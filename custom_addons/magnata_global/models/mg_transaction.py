from odoo import models, fields, api
from odoo.exceptions import UserError


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
    balance_player = fields.Float(string="Seu saldo", related="player_id.balance")
    amount = fields.Float(string="Amount", required=True)
    price = fields.Float(string="Price", required=True)
    date = fields.Datetime(string="Transaction Date", default=fields.Datetime.now)
    asset_id = fields.Many2one("magnata.global.asset", string="Asset", required=True)
    total = fields.Float(string="Total", compute="_compute_total", store=True)

    @api.depends('amount', 'price')
    def _compute_total(self):
        for record in self:
            record.total = record.amount * record.price

    @api.onchange('asset_id')
    def _onchange_asset_id(self):
        if self.asset_id:
            self.price = self.asset_id.price

    @api.model
    def create(self, vals):
        player = self.env['magnata.global.player'].browse(vals['player_id'])
        asset = self.env['magnata.global.asset'].browse(vals['asset_id'])
        asset_price = vals.get('price')
        amount = vals.get('amount')
        total = asset_price * amount

        if vals.get('transaction_type') == "buy":
            if player.balance < total:
                raise UserError("Você não tem saldo suficiente")
            if amount < asset.volume:
                raise UserError("Não tem volume suficiente disponível para compra")
            player.balance -= total
            player.write({'balance': player.balance})
        elif vals.get('transaction_type') == "sell":
            player.balance += total
            player.write({'balance': player.balance})

        return super(MagnataGlobalTransaction, self).create(vals)

