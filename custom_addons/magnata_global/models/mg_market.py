from odoo import models, fields


class MagnataGlobalMarket(models.Model):
    _name = "magnata.global.market"
    _description = "Market in Global Magnate Game"

    name = fields.Char(string="Name", required=True)
    market_type = fields.Selection(
        [
            ("stock", "Stock Market"),
            ("forex", "Foreign Exchange Market"),
            ("commodity", "Commodity Market"),
        ],
        string="Market Type",
        required=True,
    )
    description = fields.Text(string="Description")
    status = fields.Selection(
        [
            ("open", "Open"),
            ("closed", "Closed"),
        ],
        string="Status",
        default="open",
    )
