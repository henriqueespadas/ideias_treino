from odoo import models, fields


class CLQuest(models.Model):
    _name = 'dd.quest'
    _description = 'Quest Model'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    reward = fields.Integer(string='Reward')
    character_ids = fields.Many2many('dd.character', string='Characters')
