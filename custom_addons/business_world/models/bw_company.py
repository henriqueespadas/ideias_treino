from odoo import models, fields

class BusinessWorldCompany(models.Model):
    _name = 'business.world.company'
    _description = 'Business World Company'

    name = fields.Char('Company Name', required=True)
    capital = fields.Float('Capital', default=10000.0)
    reputation = fields.Float('Reputation', default=50.0) # De 0 a 100
    products_ids = fields.One2many('business.world.product', 'company_id', string='Products')

