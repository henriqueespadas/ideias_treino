from odoo import models, fields


class CSTeam(models.Model):
    _name = "cs.team"

    external_id = fields.Integer(string="ID Externo", index=True)
    name = fields.Char(string="Nome da Equipe")
    logo = fields.Char(string="URL do Logo")
