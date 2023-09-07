from odoo import api, fields, models
import requests


class PandaAPIIntegration(models.Model):
    _name = "panda.api.integration"
    _description = "Model para integrar com Panda API"

    name = fields.Char(string="Nome")

    @api.model
    def fetch_matches(self):
        url = "https://api.pandascore.co/matches"
        headers = {
            "Authorization": "Bearer " "",
        }

        response = requests.request("GET", url, headers=headers)
        if response.status_code == 200:
            matches_data = response.json()
            for match_json in matches_data:
                self.env["csg.match"].create_from_json(match_json)
                for opponent_json in match_json["opponents"]:
                    self.env["csg.opponent"].create_from_json(opponent_json)
