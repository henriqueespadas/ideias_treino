from odoo import models, fields, api
from odoo.exceptions import ValidationError


class CharacterAttributeStrong(models.Model):
    _name = "dd.attribute.strength"
    _description = "Strength Attribute Model"

    strength_name = fields.Char(string="Attribute Name", default="Força", readonly=True)
    strength_value = fields.Integer(string="Value", required=True)
    strength_modifier = fields.Integer(
        string="Modifier", compute="_compute_modifier", store=True
    )
    strength_description = fields.Text(
        string="Description",
        default="A Força mede o poder físico bruto, treinamento atlético e a extensão à qual você pode exercer força bruta.",
    )
    strength_min_value = fields.Integer(
        string="Minimum Value", default=1, readonly=True
    )
    strength_max_value = fields.Integer(
        string="Maximum Value", default=20, readonly=True
    )

    @api.depends("strength_value")
    def _compute_modifier(self):
        for record in self:
            record.strength_modifier = (record.strength_value - 10) // 2

    @api.constrains("strength_value")
    def _check_value_range(self):
        for record in self:
            if (
                record.strength_value < record.strength_min_value
                or record.strength_value > record.strength_max_value
            ):
                raise ValidationError(
                    "O valor do atributo Força deve estar entre %s e %s."
                    % (record.strength_min_value, record.strength_max_value)
                )
