from odoo import models, fields


class MagnataGlobalAsset(models.Model):
    _name = "magnata.global.asset"
    name = fields.Char(string="Nome da Empresa")
    symbol = fields.Char(string="Símbolo")
    price = fields.Float(string="Preço Atual")
    volume = fields.Integer(string="Volume")
