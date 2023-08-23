from odoo import models, fields


class MagnataPlayerPortfolio(models.Model):
    _name = "magnata.global.portfolio"

    player_id = fields.Many2one("magnata.global.player", string="Jogador")
    asset_id = fields.Many2one("magnata.global.asset", string="Ativo")
    quantity = fields.Float("Quantidade")
    purchase_price = fields.Float("Preço de Compra")
