from odoo import models, fields
import requests

class AlphaVantageAPI:
    ALPHA_VANTAGE_ENDPOINT = "https://www.alphavantage.co/query"

    def __init__(self, api_key):
        self.api_key = api_key

    def get_stock_price(self, symbol):
        params = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": symbol,
            "interval": "5min",
            "apikey": self.api_key,
        }
        response = requests.get(self.ALPHA_VANTAGE_ENDPOINT, params=params)
        data = response.json()

        price = data['Time Series (5min)'][list(data['Time Series (5min)'].keys())[0]]['1. open']
        return float(price)

