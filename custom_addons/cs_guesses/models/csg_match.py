from odoo import models, fields, api

from core.odoo.tools import datetime


class CSMatch(models.Model):
    _name = 'csg.match'

    begin_at = fields.Datetime(string='Data e Hora de Início')
    detailed_stats = fields.Boolean(string='Estatísticas Detalhadas')
    draw = fields.Boolean(string='Empate')
    end_at = fields.Datetime(string='Data e Hora de Término')
    forfeit = fields.Boolean(string='Desistência')
    game_advantage = fields.Boolean(string='Vantagem de Jogo')
    match_id = fields.Integer(string='ID da Partida', index=True)
    name = fields.Char(string='Nome da Partida')
    number_of_games = fields.Integer(string='Número de Jogos')
    scheduled_at = fields.Datetime(string='Agendada para')
    status = fields.Char(string='Status')
    league_id = fields.Integer(string='ID da Liga')
    league_name = fields.Char(string='Nome da Liga')
    serie_id = fields.Integer(string='ID da Série')
    serie_begin_at = fields.Datetime(string='Início da Série')
    serie_end_at = fields.Datetime(string='Fim da Série')
    opponents = fields.Many2many('csg.opponent', string='Oponentes')

    @api.model
    def convert_datetime(self, date_str):
        try:
            if date_str is not None:
                return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M:%S")
        except ValueError as e:
            return None

    @api.model
    def create_from_json(self, match_json):
        match_id = match_json['id']
        existing_match = self.env['csg.match'].search([('match_id', '=', match_id)], limit=1)

        if existing_match:
            vals_to_update = {
                'begin_at': self.convert_datetime(match_json['begin_at']),
                'detailed_stats': match_json['detailed_stats'],
                'draw': match_json['draw'],
                'end_at': self.convert_datetime(match_json['end_at']),
                'forfeit': match_json['forfeit'],
                'game_advantage': match_json['game_advantage'],
                'name': match_json['name'],
                'number_of_games': match_json['number_of_games'],
                'scheduled_at': self.convert_datetime(match_json['scheduled_at']),
                'status': match_json['status'],
                'league_id': match_json['league']['id'],
                'league_name': match_json['league']['name'],
                'serie_id': match_json['serie']['id'],
                'serie_begin_at': self.convert_datetime(match_json['serie']['begin_at']),
                'serie_end_at': self.convert_datetime(match_json['serie']['end_at']),
                'opponents': [(6, 0, [self.env['csg.opponent'].create_from_json(opponent_json).id for opponent_json in match_json['opponents']])]
            }

            vals_to_update = {key: val for key, val in vals_to_update.items() if val is not None}
            existing_match.write(vals_to_update)
            return existing_match
        else:
            values = {
                'begin_at': self.convert_datetime(match_json['begin_at']),
                'detailed_stats': match_json['detailed_stats'],
                'draw': match_json['draw'],
                'end_at': self.convert_datetime(match_json['end_at']),
                'forfeit': match_json['forfeit'],
                'game_advantage': match_json['game_advantage'],
                'match_id': match_id,
                'name': match_json['name'],
                'number_of_games': match_json['number_of_games'],

                'scheduled_at': self.convert_datetime(match_json['scheduled_at']),
                'status': match_json['status'],
                'league_id': match_json['league']['id'],
                'league_name': match_json['league']['name'],
                'serie_id': match_json['serie']['id'],
                'serie_begin_at': self.convert_datetime(match_json['serie']['begin_at']),
                'serie_end_at': self.convert_datetime(match_json['serie']['end_at']),
                'opponents': [(6, 0, [self.env['csg.opponent'].create_from_json(opponent_json).id for opponent_json in match_json['opponents']])]
            }

            values = {key: val for key, val in values.items() if val is not None}
            return self.create(values)
