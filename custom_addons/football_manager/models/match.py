from odoo import models, fields
import random


class Match(models.Model):
    _name = "football.manager.match"

    championship_id = fields.Many2one(
        "football.manager.championship", "Championship", required=True
    )
    date = fields.Date("Date", required=True)
    home_team_id = fields.Many2one("football.manager.team", "Home Team", required=True)
    away_team_id = fields.Many2one("football.manager.team", "Away Team", required=True)
    home_team_score = fields.Integer("Home Team Score", default=0)
    away_team_score = fields.Integer("Away Team Score", default=0)
    state = fields.Selection(
        [
            ("scheduled", "Scheduled"),
            ("completed", "Completed"),
            ("canceled", "Canceled"),
        ],
        default="scheduled",
        string="Status",
    )
    result = fields.Char("Resultado", readonly=True)

    def simulate_match(self):
        for match in self:
            home_team_attack = sum(
                player.attack for player in match.home_team_id.player_ids
            )
            away_team_attack = sum(
                player.attack for player in match.away_team_id.player_ids
            )

            home_team_defense = sum(
                player.defense for player in match.home_team_id.player_ids
            )
            away_team_defense = sum(
                player.defense for player in match.away_team_id.player_ids
            )

            home_team_goals = max(
                0,
                int((home_team_attack - away_team_defense) * random.uniform(0.01, 0.1)),
            )
            away_team_goals = max(
                0,
                int((away_team_attack - home_team_defense) * random.uniform(0.01, 0.1)),
            )

            match.result = f"{home_team_goals} - {away_team_goals}"
