from odoo import http
from odoo.http import request


class CharacterController(http.Controller):
    @http.route("/create_character", type="http", auth="user", website=True)
    def create_character(self, **kwargs):
        return request.render("dd.create_character_template")

    @http.route(
        "/save_character", type="http", auth="user", method=["POST"], website=True
    )
    def save_character(self, **post):
        vals = {
            "name": post.get("name"),
            "strength": post.get("strength"),
            "agility": post.get("agility"),
        }
        request.env["dd.character"].sudo().create(vals)
        return "Personagem criado"
