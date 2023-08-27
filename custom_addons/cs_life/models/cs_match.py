from odoo import models, fields, api
import requests
import json


class CSMatch(models.Model):
    _name = 'cs.match'

    external_id = fields.Integer(string='ID Externo', index=True)
    time = fields.Datetime(string='Data e Hora da Partida')
    stars = fields.Integer(string='Estrelas')
    maps = fields.Char(string='Mapas')

    event_id = fields.Many2one('cs.event', string='Evento')
    team_ids = fields.Many2many('cs.team', string='Equipes')

    @api.model
    def fetch_from_csgo_api(self):
        url = 'https://hltv-api.vercel.app/api/matches'
        response = requests.get(url)
        if response.status_code == 200:
            print('200')
            data = json.loads(response.text)

            event = self.env['cs.event'].create({
                'name': data['event']['name'],
                'logo': data['event']['logo']
            })

            team_list = []
            for team_data in data['teams']:
                team = self.env['cs.team'].create({
                    'external_id': team_data['id'],
                    'name': team_data['name'],
                    'logo': team_data['logo']
                })
                team_list.append(team.id)

            self.env['cs.match'].create({
                'external_id': data['id'],
                'time': fields.Datetime.from_string(data['time']),
                'stars': data['stars'],
                'maps': data['maps'],
                'event_id': event.id,
                'team_ids': [(6, 0, team_list)]
            })
