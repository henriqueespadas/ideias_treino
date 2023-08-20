from odoo import models, fields


class MagnataGlobalTransaction(models.Model):
    _name = "magnata.global.transaction"
    _description = "Transaction in Global Magnate Game"

    player_id = fields.Many2one("magnata.global.player", string="Player", required=True)
    market_id = fields.Many2one("magnata.global.market", string="Market", required=True)
    transaction_type = fields.Selection(
        [
            ("buy", "Buy"),
            ("sell", "Sell"),
        ],
        string="Transaction Type",
        required=True,
    )
    amount = fields.Float(string="Amount", required=True)
    price = fields.Float(string="Price", required=True)
    date = fields.Datetime(string="Transaction Date", default=fields.Datetime.now)
