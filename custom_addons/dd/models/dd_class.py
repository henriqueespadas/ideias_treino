from odoo import models, fields


class DDClass(models.Model):
    _name = "dd.class"

    class_name = fields.Char(string="Nome da Classe")
    class_skill = fields.Char(string="Habilidade da Classe")
    class_hit_points = fields.Integer(string="Pontos de Vida")
