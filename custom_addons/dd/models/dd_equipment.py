from odoo import models, fields


class DDEquipment(models.Model):
    _name = "dd.equipment"
    _description = "Equipment Model"

    equipment_name = fields.Char(string="Name", required=True)
    equipment_type = fields.Selection(
        [("weapon", "Weapon"), ("armor", "Armor")], string="Type"
    )
    character_id = fields.Many2one("dd.character", string="Character")
    equipment_class_id = fields.Many2one("dd.class", string="Class")
