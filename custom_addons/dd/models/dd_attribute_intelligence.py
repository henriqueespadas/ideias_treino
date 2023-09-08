from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CharacterAttributeIntelligence(models.Model):
    _name = 'dd.attribute.intelligence'
    _description = 'Intelligence Attribute Model'

    intelligence_name = fields.Char(string='Attribute Name', default='Inteligência', readonly=True)
    intelligence_value = fields.Integer(string='Value', required=True)
    intelligence_modifier = fields.Integer(string='Modifier', compute='_compute_modifier', store=True)
    intelligence_description = fields.Text(string='Description', default='A Inteligência mede a acuidade mental, precisão de raciocínio, e a capacidade de aprender.')
    intelligence_min_value = fields.Integer(string='Minimum Value', default=1, readonly=True)
    intelligence_max_value = fields.Integer(string='Maximum Value', default=20, readonly=True)

    @api.depends('intelligence_value')
    def _compute_modifier(self):
        for record in self:
            record.intelligence_modifier = (record.intelligence_value - 10) // 2

    @api.constrains('intelligence_value')
    def _check_value_range(self):
        for record in self:
            if record.intelligence_value < record.intelligence_min_value or record.intelligence_value > record.intelligence_max_value:
                raise ValidationError("O valor do atributo Inteligência deve estar entre %s e %s." % (record.intelligence_min_value, record.intelligence_max_value))
