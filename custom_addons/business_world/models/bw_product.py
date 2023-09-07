from odoo import models, fields


class BusinessWorldProduct(models.Model):
    _name = "business.world.product"
    _description = "Business World Product"

    name = fields.Char("Product Name", required=True)
    price = fields.Float("Price")
    company_id = fields.Many2one("business.world.company", string="Company")
