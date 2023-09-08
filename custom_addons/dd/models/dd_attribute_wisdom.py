from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CharacterAttributeWisdom(models.Model):
    _name = 'dd.attribute.wisdom'
    _description = 'Wisdom Attribute Model'

    wisdom_name = fields.Char(string='Attribute Name', default='Sabedoria', readonly=True)
    wisdom_value = fields.Integer(string='Value', required=True)
    wisdom_modifier = fields.Integer(string='Modifier', compute='_compute_modifier', store=True)
    wisdom_description = fields.Text(string='Description', default='A Sabedoria mede a percepção, intuição e empatia.')
    wisdom_min_value = fields.Integer(string='Minimum Value', default=1, readonly=True)
    wisdom_max_value = fields.Integer(string='Maximum Value', default=20, readonly=True)

    @api.depends('wisdom_value')
    def _compute_modifier(self):
        for record in self:
            record.wisdom_modifier = (record.wisdom_value - 10) // 2

    @api.constrains('wisdom_value')
    def _check_value_range(self):
        for record in self:
            if record.wisdom_value < record.wisdom_min_value or record.wisdom_value > record.wisdom_max_value:
                raise ValidationError("O valor do atributo Sabedoria deve estar entre %s e %s." % (record.wisdom_min_value, record.wisdom_max_value))
