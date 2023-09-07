from odoo import models, fields


class DDQuest(models.Model):
    _name = "dd.quest"
    _description = "Quest Model"

    quest_name = fields.Char(string="Name", required=True)
    quest_description = fields.Text(string="Description")
    quest_reward = fields.Integer(string="Reward")
    quest_character_ids = fields.Many2many("dd.character", string="Characters")
