from odoo import models, fields

class Monster(models.Model):
    _name = 'dd.monster'
    _description = 'Monster Model'

    monster_name = fields.Char(string='Name', required=True)
    monster_hp = fields.Integer(string='Health Points', required=True)
    monster_type = fields.Selection([
        ('dragon', 'Dragon'),
        ('goblin', 'Goblin'),
        ('undead', 'Undead')
    ], string='Type', required=True)
    skill_ids = fields.Many2many('dd.skill', string='Skills')
