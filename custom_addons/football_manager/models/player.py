import random

from odoo import models, fields


class Player(models.Model):
    _name = 'football.manager.player'

    name = fields.Char('Player Name', required=True)
    position = fields.Selection([
        ('gk', 'Goleiro'),
        ('rb', 'Lateral-direito'),
        ('cb', 'Zagueiro-central'),
        ('lb', 'Lateral-esquerdo'),
        ('cdm', 'Volante'),
        ('cm', 'Meia-central'),
        ('cam', 'Meia-atacante'),
        ('rm', 'Meia-direita'),
        ('lm', 'Meia-esquerda'),
        ('st', 'Atacante'),
        ('rw', 'Ponta-direita'),
        ('lw', 'Ponta-esquerda'),
    ], 'Position')
    age = fields.Integer('Age')
    team_id = fields.Many2one('football.manager.team', 'Team')
    salary = fields.Integer('Salary')

    # Atributos de habilidade
    attack = fields.Integer('Attack', default=50)
    defense = fields.Integer('Defense', default=50)
    shooting = fields.Integer('Shooting', default=50)
    passing = fields.Integer('Passing', default=50)
    speed = fields.Integer('Speed', default=50)
    stamina = fields.Integer('Stamina', default=50)
    strength = fields.Integer('Strength', default=50)
    ball_control = fields.Integer('Ball Control', default=50)
    dribbling = fields.Integer('Dribbling', default=50)
    crossing = fields.Integer('Crossing', default=50)
    heading = fields.Integer('Heading', default=50)
    marking = fields.Integer('Marking', default=50)
    tackling = fields.Integer('Tackling', default=50)
    positioning = fields.Integer('Positioning', default=50)
    vision = fields.Integer('Vision', default=50)
    free_kick = fields.Integer('Free Kick', default=50)
    penalty_kick = fields.Integer('Penalty Kick', default=50)
    corner_kick = fields.Integer('Corner Kick', default=50)
    reflexes = fields.Integer('Reflexes', default=50)
    communication = fields.Integer('Communication', default=50)


