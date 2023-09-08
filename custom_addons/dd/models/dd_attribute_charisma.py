from odoo import models, fields, api
from odoo.exceptions import ValidationError


class CharacterAttributeCharisma(models.Model):
    _name = 'dd.attribute.charisma'
    _description = 'Charisma Attribute Model'

    charisma_name = fields.Char(string='Attribute Name', default='Carisma', readonly=True)
    charisma_value = fields.Integer(string='Value', required=True)
    charisma_modifier = fields.Integer(string='Modifier', compute='_compute_modifier', store=True)
    charisma_description = fields.Text(string='Description', default='O Carisma mede a força de personalidade, persuasão, e liderança.')
    charisma_min_value = fields.Integer(string='Minimum Value', default=1, readonly=True)
    charisma_max_value= fields.Integer(string='Maximum Value', default=20, readonly=True)

    @api.depends('charisma_value')
    def _compute_modifier(self):
        for record in self:
            record.charisma_modifier = (record.charisma_value - 10) // 2

    @api.constrains('charisma_value')
    def _check_value_range(self):
        for record in self:
            if record.charisma_value < record.charisma_min_value or record.charisma_value > record.charisma_max_value:
                raise ValidationError("O valor do atributo Carisma deve estar entre %s e %s." % (record.charisma_min_value, record.charisma_max_value))
