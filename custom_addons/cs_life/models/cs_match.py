from odoo import models, fields, api
import requests
import json
from dateutil.parser import parse

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
        url = 'https://hltv-api.vercel.app/api/matches.json'
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Erro ao buscar dados da API: {e}")
            return

        if response.status_code == 200:
            data = json.loads(response.text)

            if type(data) is list:
                for match in data:
                    self._process_match(match)

            elif type(data) is dict:
                self._process_match(data)
            else:
                print("Formato de dados desconhecido")

    def _process_match(self, match_data):
        try:
            event = self.env['cs.event'].create({
                'name': match_data['event']['name'],
                'logo': match_data['event']['logo']
            })

            team_list = []
            for team_data in match_data['teams']:
                team = self.env['cs.team'].create({
                    'external_id': team_data['id'],
                    'name': team_data['name'],
                    'logo': team_data['logo']
                })
                team_list.append(team.id)

            self.env['cs.match'].create({
                'external_id': match_data['id'],
                'time': parse(match_data['time']).strftime('%Y-%m-%d %H:%M:%S'),
                'stars': match_data['stars'],
                'maps': match_data['maps'],
                'event_id': event.id,
                'team_ids': [(6, 0, team_list)],
            })

        except KeyError as e:
            print(f"Chave não encontrada: {e}")
