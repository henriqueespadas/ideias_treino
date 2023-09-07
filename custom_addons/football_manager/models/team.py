import random

from odoo import models, fields, api


class Team(models.Model):
    _name = "football.manager.team"

    name = fields.Char("Team Name", required=True)
    coach = fields.Char("Coach")
    league = fields.Char("League")
    player_ids = fields.One2many("football.manager.player", "team_id", "Players")

    @api.model
    def create(self, vals):
        team = super(Team, self).create(vals)

        positions = [
            "gk",
            "rb",
            "cb",
            "lb",
            "cdm",
            "cm",
            "cam",
            "rm",
            "lm",
            "st",
            "rw",
            "lw",
        ]

        # Criar 18 jogadores com habilidades aleatórias
        for i in range(18):
            position = random.choice(positions)
            player_vals = {
                "name": f"Player {i + 1}",
                "team_id": team.id,
                "position": position,
                "age": random.randint(18, 35),
                "salary": random.randint(50, 5000),
                "attack": random.randint(1, 100),
                "defense": random.randint(1, 100),
                "shooting": random.randint(1, 100),
                "passing": random.randint(1, 100),
                "speed": random.randint(1, 100),
                "stamina": random.randint(1, 100),
                "strength": random.randint(1, 100),
                "ball_control": random.randint(1, 100),
                "dribbling": random.randint(1, 100),
                "crossing": random.randint(1, 100),
                "heading": random.randint(1, 100),
                "marking": random.randint(1, 100),
                "tackling": random.randint(1, 100),
                "positioning": random.randint(1, 100),
                "vision": random.randint(1, 100),
                "free_kick": random.randint(1, 100),
                "penalty_kick": random.randint(1, 100),
                "corner_kick": random.randint(1, 100),
                "reflexes": random.randint(1, 100),
                "communication": random.randint(1, 100),
            }
            self.env["football.manager.player"].create(player_vals)

        return team
