from odoo import models, fields, api
from odoo.exceptions import ValidationError


class CharacterAttributeConstitution(models.Model):
    _name = "dd.attribute.constitution"
    _description = "Constitution Attribute Model"

    constitution_name = fields.Char(
        string="Attribute Name", default="Constituição", readonly=True
    )
    constitution_value = fields.Integer(string="Value", required=True)
    constitution_modifier = fields.Integer(
        string="Modifier", compute="_compute_modifier", store=True
    )
    constitution_min_value = fields.Integer(
        string="Minimum Value", default=1, readonly=True
    )
    constitution_max_value = fields.Integer(
        string="Maximum Value", default=20, readonly=True
    )
    constitution_description = fields.Text(
        string="Description",
        default="A Constituição mede a saúde, resistência e vitalidade do personagem.",
    )

    @api.depends("constitution_value")
    def _compute_modifier(self):
        for record in self:
            record.constitution_modifier = (record.constitution_value - 10) // 2

    @api.constrains("constitution_value")
    def _check_value_range(self):
        for record in self:
            if (
                record.constitution_value < record.constitution_min_value
                or record.constitution_value > record.constitution_max_value
            ):
                raise ValidationError(
                    "O valor do atributo Constituição deve estar entre %s e %s."
                    % (record.constitution_min_value, record.constitution_max_value)
                )
