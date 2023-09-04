from odoo import models, fields


class DDEquipment(models.Model):
    _name = 'dd.equipment'
    _description = 'Equipment Model'

    name = fields.Char(string='Name', required=True)
    type = fields.Selection([('weapon', 'Weapon'), ('armor', 'Armor')], string='Type')
    character_id = fields.Many2one('dd.character', string='Character')
