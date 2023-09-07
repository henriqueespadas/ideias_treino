from odoo import models, fields


class CSEvent(models.Model):
    _name = "cs.event"

    name = fields.Char(string="Nome do Evento")
    logo = fields.Char(string="URL do Logo")
