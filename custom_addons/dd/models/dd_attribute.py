from odoo import models, fields, api
from odoo.exceptions import ValidationError


class DDAttribute(models.Model):
    _name = "dd.attribute"
    _description = "Attribute Model"

    attribute_name = fields.Char(string="Name", required=True)
    attribute_description = fields.Text(string="Description")
    attribute_value = fields.Integer(string="Value", required=True)
    attribute_modifier = fields.Integer(
        string="Modifier", compute="_compute_modifier", store=True
    )
    attribute_character_ids = fields.Many2many("dd.character", string="Players")

    @api.depends("attribute_value")
    def _compute_modifier(self):
        for record in self:
            record.attribute_modifier = (record.attribute_value - 10) // 2

    @api.constrains("attribute_value")
    def _check_value_range(self):
        for record in self:
            if not (1 <= record.attribute_value <= 20):
                raise ValidationError("O valor do atributo deve estar entre 1 e 20.")
