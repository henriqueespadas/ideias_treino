from odoo import models, fields, api, SUPERUSER_ID
import requests
import json


class MagnataGlobalAsset(models.Model):
    _name = 'magnata.global.asset'
    name = fields.Char(string='Nome da Empresa')
    symbol = fields.Char(string='Símbolo')
    price = fields.Float(string='Preço Atual')
    volume = fields.Integer(string='Volume')


class MagnataGlobalAssetUpdate(models.Model):
    _name = 'magnata.global.asset_update'

    @api.model
    def update_assets(self):
        symbols = ['AAPL', 'MSFT', 'AMZN', 'GOOGL']

        for symbol in symbols:
            data = self.call_alpha_vantage_api(symbol)
            asset = self.env['magnata.global.asset'].search([('symbol', '=', symbol)], limit=1)
            if asset:
                asset.write({
                    'price': data['price'],
                    'volume': data['volume']
                })
            else:
                self.env['magnata.global.asset'].create({
                    'name': symbol,
                    'symbol': symbol,
                    'price': data['price'],
                    'volume': data['volume']
                })

    def call_alpha_vantage_api(self, symbol):
        ALPHA_VANTAGE_API_URL = 'https://www.alphavantage.co/query'
        ALPHA_VANTAGE_API_KEY = 'QEW6JVZJGMJTTATH'

        params = {
            'function': 'TIME_SERIES_INTRADAY',
            'symbol': symbol,
            'interval': '5min',
            'apikey': ALPHA_VANTAGE_API_KEY
        }

        response = requests.get(ALPHA_VANTAGE_API_URL, params=params)
        data = json.loads(response.text)

        if 'Time Series (5min)' in data:
            last_record_key = next(iter(data['Time Series (5min)']))
        else:
            print("Key 'Time Series (5min)' not found in data")
        last_record_data = data['Time Series (5min)'][last_record_key]

        return {
            'price': float(last_record_data['4. close']),
            'volume': int(last_record_data['5. volume'])
        }
















