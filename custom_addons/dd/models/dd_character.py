from odoo import models, fields, api


class DDCharacter(models.Model):
    _name = "dd.character"

    character_name = fields.Char(string="Nome")
    character_level = fields.Integer(string="Nível", default=1)
    character_stamina = fields.Float(string="Energia", default=100)
    character_class_id = fields.Many2one("dd.class", string="Raça")
    character_attribute_charisma = fields.Many2one(
        "dd.attribute.charisma", string="Carisma"
    )
    character_attribute_constitution = fields.Many2one(
        "dd.attribute.constitution", string="Constituição"
    )
    character_attribute_dexterity = fields.Many2one(
        "dd.attribute.dexterity", string="Destreza"
    )
    character_attribute_intelligence = fields.Many2one(
        "dd.attribute.intelligence", string="Inteligência"
    )
    character_attribute_strength = fields.Many2one(
        "dd.attribute.strength", string="Força"
    )
    character_attribute_wisdom = fields.Many2one(
        "dd.attribute.wisdom", string="Sabedoria"
    )
    character_attribute_charisma_value = fields.Integer(
        string="Carisma", related="character_attribute_charisma.charisma_value"
    )
    character_attribute_constitution_value = fields.Integer(
        string="Constituição",
        related="character_attribute_constitution.constitution_value",
    )
    character_attribute_dexterity_value = fields.Integer(
        string="Destreza", related="character_attribute_dexterity.dexterity_value"
    )
    character_attribute_intelligence_value = fields.Integer(
        string="Inteligência",
        related="character_attribute_intelligence.intelligence_value",
    )
    character_attribute_strength_value = fields.Integer(
        string="Força", related="character_attribute_strength.strength_value"
    )
    character_attribute_wisdom_value = fields.Integer(
        string="Sabedoria", related="character_attribute_wisdom.wisdom_value"
    )
    character_attribute_charisma_modifier = fields.Integer(
        string="Carisma", related="character_attribute_charisma.charisma_modifier"
    )
    character_hit_points = fields.Integer(string="Pontos de Vida", default=0)
    character_hit_points_max = fields.Integer(string="Pontos de Vida Máximo", default=0)
    character_experience = fields.Integer(string="Experiência", default=0)
    character_hit_points_temporary = fields.Integer(string="Pontos de Vida Temporários")

    def level_up(self):
        self.character_level += 1
        self.character_stamina = 100
        return True
