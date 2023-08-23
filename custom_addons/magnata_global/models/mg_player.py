from odoo import models, fields, api
from odoo.exceptions import ValidationError


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
    user_id = fields.Many2one('res.users', string='User', required=True, ondelete='cascade', index=True)

    @api.constrains('user_id')
    def _check_unique_user_id(self):
        for record in self:
            if self.search_count([('user_id', '=', record.user_id.id)]) > 1:
                raise ValidationError('Um usuário só pode ter um jogador associado.')

    @api.model
    def create(self, vals):
        vals['user_id'] = self.env.user.id
        return super(MagnataGlobalPlayer, self).create(vals)



