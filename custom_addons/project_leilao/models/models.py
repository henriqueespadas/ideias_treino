from odoo import models, fields


class Leilao(models.Model):
    _name = 'leilao.leilao'
    _description = 'Leilão'

    name = fields.Char(string='Nome', required=True)
    start_date = fields.Date(string='Data de Início')
    end_date = fields.Date(string='Data de Encerramento')
    status = fields.Selection([
        ('draft', 'Rascunho'),
        ('open', 'Aberto'),
        ('closed', 'Encerrado'),
    ], string='Status', default='draft')


class Produto(models.Model):
    _name = 'leilao.produto'
    _description = 'Produto'

    name = fields.Char(string='Nome', required=True)
    description = fields.Text(string='Descrição')
    starting_price = fields.Float(string='Valor Inicial')
    image = fields.Binary(string='Imagem')
    auction_id = fields.Many2one('leilao.leilao', string='Leilão')


class Lance(models.Model):
    _name = 'leilao.lance'
    _description = 'Lance'

    bid_amount = fields.Float(string='Valor do Lance')
    bid_date = fields.Datetime(string='Data/Hora do Lance', default=fields.Datetime.now)
    user_id = fields.Many2one('res.users', string='Usuário', required=True)
    product_id = fields.Many2one('leilao.produto', string='Produto', required=True)