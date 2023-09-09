from odoo import models, fields, api
from odoo.exceptions import ValidationError


class CharacterAttributeDexterity(models.Model):
    _name = "dd.attribute.dexterity"
    _description = "Dexterity Attribute Model"

    dexterity_name = fields.Char(
        string="Attribute Name", default="Destreza", readonly=True
    )
    dexterity_value = fields.Integer(string="Value", required=True)
    dexterity_modifier = fields.Integer(
        string="Modifier", compute="_compute_modifier", store=True
    )
    dexterity_description = fields.Text(
        string="Description",
        default="A Destreza mede a agilidade, os reflexos e o equilíbrio.",
    )
    dexterity_min_value = fields.Integer(
        string="Minimum Value", default=1, readonly=True
    )
    dexterity_max_value = fields.Integer(
        string="Maximum Value", default=20, readonly=True
    )

    @api.depends("dexterity_value")
    def _compute_modifier(self):
        for record in self:
            record.modifier = (record.dexterity_value - 10) // 2

    @api.constrains("dexterity_value")
    def _check_value_range(self):
        for record in self:
            if (
                record.dexterity_value < record.dexterity_min_value
                or record.dexterity_value > record.dexterity_max_value
            ):
                raise ValidationError(
                    "O valor do atributo Destreza deve estar entre %s e %s."
                    % (record.dexterity_min_value, dexterity_max_value.max_value)
                )
