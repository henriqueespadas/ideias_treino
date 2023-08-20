from odoo import models, fields, api


class BusinessWorldEmployee(models.Model):
    _name = 'business.world.employee'
    _description = 'Business World Employee'

    name = fields.Char('Employee Name', required=True)
    salary = fields.Float('Salary')
    skill_level = fields.Selection([('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='low')
    company_id = fields.Many2one('business.world.company', string='Company')
