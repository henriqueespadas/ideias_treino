from odoo import api, fields, models
import requests

class PandaAPIIntegration(models.Model):
    _name = 'panda.api.integration'
    _description = 'Model para integrar com Panda API'

    name = fields.Char(string='Nome')

    @api.model
    def fetch_matches(self):
        url = "https://api.pandascore.co/matches"
        headers = {
            'Authorization': 'Bearer d6dg_fLFTi_R0jfdTa6qfnZNNf3rQtPTrdJ-9G4zOhGN7hix36I',
        }

        response = requests.request("GET", url, headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            matches_data = response.json()
            for match_json in matches_data:
                match = self.env['csg.match'].create_from_json(match_json)
                print('match', match)

                for opponent_json in match_json['opponents']:
                    opponent = self.env['csg.opponent'].create_from_json(opponent_json)
                    print('opponent', opponent)



