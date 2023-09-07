from odoo import models, fields


class DDSkill(models.Model):
    _name = "dd.skill"
    _description = "Skill Model"

    skill_name = fields.Char(string="Name", required=True)
    skill_damage = fields.Integer(string="Damage")
    skill_range = fields.Integer(string="Range")
    skill_class_id = fields.Many2one("dd.class", string="Class")
