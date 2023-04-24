from odoo import models, fields


class Championship(models.Model):
    _name = 'football.manager.championship'

    name = fields.Char('Championship Name', required=True)
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    team_ids = fields.Many2many('football.manager.team', 'championship_team_rel', 'championship_id', 'team_id', 'Teams')
