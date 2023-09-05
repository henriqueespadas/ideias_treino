from odoo import models, fields, api


class DDCharacter(models.Model):
    _name = 'dd.character'

    character_name = fields.Char(string='Nome')
    character_level = fields.Integer(string='Nível', default=1)
    character_stamina = fields.Float(string='Energia', default=100)
    character_class_id = fields.Many2one('dd.class', string='Classe')

    def level_up(self):
        self.character_level += 1
        self.character_stamina = 100
        return True
