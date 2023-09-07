from odoo import models, fields, api


class DDCharacter(models.Model):
    _name = 'dd.character'

    character_name = fields.Char(string='Nome')
    character_level = fields.Integer(string='Nível', default=1)
    character_stamina = fields.Float(string='Energia', default=100)
    character_class_id = fields.Many2one('dd.class', string='Classe')
    character_strong = fields.Many2one('dd.atribute.strong', string='Força')
    character_dexterity = fields.Many2one('dd.atribute.dexterity', string='Destreza')
    character_intelligence = fields.Many2one('dd.atribute.intelligence', string='Inteligência')
    character_wisdom = fields.Many2one('dd.atribute.wisdom', string='Sabedoria')
    character_charisma = fields.Many2one('dd.atribute.charisma', string='Carisma')
    character_constitution = fields.Many2one('dd.atribute.constitution', string='Constituição')

    def level_up(self):
        self.character_level += 1
        self.character_stamina = 100
        return True
