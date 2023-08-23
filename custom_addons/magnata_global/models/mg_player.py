from odoo import models, fields


class MagnataGlobalPlayer(models.Model):
    _name = "magnata.global.player"
    _description = "Player in Global Magnate Game"

    name = fields.Char(string="Name", required=True)
    balance = fields.Float(string="Balance", default=10000.0, readonly=True)
    level = fields.Integer(string="Level", default=1)
    experience = fields.Integer(string="Experience", default=0)
    transactions_ids = fields.One2many(
        "magnata.global.transaction", "player_id", string="Transações"
    )
    portfolio_ids = fields.One2many(
        "magnata.global.portfolio", "player_id", string="Portfólio"
    )
