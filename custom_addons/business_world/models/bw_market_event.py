from odoo import models, fields


class BusinessWorldMarketEvent(models.Model):
    _name = "business.world.market.event"
    _description = "Business World Market Event"

    name = fields.Char("Event Name", required=True)
    impact = fields.Selection(
        [("positive", "Positive"), ("negative", "Negative")], default="positive"
    )
    magnitude = fields.Float("Magnitude")
