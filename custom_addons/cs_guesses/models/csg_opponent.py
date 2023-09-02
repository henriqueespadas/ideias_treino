from odoo import fields, models, api

class Opponent(models.Model):
    _name = 'csg.opponent'
    _description = 'Modelo para armazenar informações sobre oponentes'

    opponent_id = fields.Integer(string='ID do Oponente', index=True)
    acronym = fields.Char(string='Acrônimo')
    image_url = fields.Char(string='URL da Imagem')
    location = fields.Char(string='Localização')
    name = fields.Char(string='Nome')
    slug = fields.Char(string='Slug')
    type = fields.Char(string='Tipo')
    match_ids = fields.Many2many('csg.match', string='Partidas')

    @api.model
    def create_from_json(self, opponent_json):
        opponent_id = opponent_json['opponent']['id']
        existing_opponent = self.env['csg.opponent'].search([('opponent_id', '=', opponent_id)], limit=1)

        if existing_opponent:
            vals_to_update = {
                'acronym': opponent_json['opponent'].get('acronym', False),
                'image_url': opponent_json['opponent'].get('image_url', False),
                'location': opponent_json['opponent'].get('location', False),
                'name': opponent_json['opponent']['name'],
                'slug': opponent_json['opponent']['slug'],
                'type': opponent_json['type'],
            }
            existing_opponent.write(vals_to_update)
            return existing_opponent
        else:
            values = {
                'opponent_id': opponent_id,
                'acronym': opponent_json['opponent'].get('acronym', False),
                'image_url': opponent_json['opponent'].get('image_url', False),
                'location': opponent_json['opponent'].get('location', False),
                'name': opponent_json['opponent']['name'],
                'slug': opponent_json['opponent']['slug'],
                'type': opponent_json['type'],
            }
            return self.create(values)

    def button_open_opponent(self):
        self.ensure_one()
        return {
            'name': 'Abrir Oponente',
            'type': 'ir.actions.act_window',
            'res_model': 'csg.opponent',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'current',
        }
