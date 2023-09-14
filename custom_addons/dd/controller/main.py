from odoo import http
from odoo.http import request


class MainController(http.Controller):
    @http.route("/index", type="http", auth="user", website=True)
    def index(self, **kwargs):
        return request.render("dd.dd_index_template")

    @http.route("/create_character", type="http", auth="user", website=True)
    def create_character(self, **kwargs):
        classes = request.env["dd.class"].sudo().search([])
        return request.render("dd.create_character_template", {"classes": classes})

    @http.route(
        "/save_character", type="http", auth="user", method=["POST"], website=True
    )
    def save_character(self, **post):
        charisma_id = (
            request.env["dd.attribute.charisma"]
            .sudo()
            .create(
                {
                    "charisma_value": int(
                        post.get("character_attribute_charisma_value", 0)
                    )
                }
            )
            .id
        )
        constitution_id = (
            request.env["dd.attribute.constitution"]
            .sudo()
            .create(
                {
                    "constitution_value": int(
                        post.get("character_attribute_constitution_value", 0)
                    )
                }
            )
            .id
        )
        dexterity_id = (
            request.env["dd.attribute.dexterity"]
            .sudo()
            .create(
                {
                    "dexterity_value": int(
                        post.get("character_attribute_dexterity_value", 0)
                    )
                }
            )
            .id
        )
        intelligence_id = (
            request.env["dd.attribute.intelligence"]
            .sudo()
            .create(
                {
                    "intelligence_value": int(
                        post.get("character_attribute_intelligence_value", 0)
                    )
                }
            )
            .id
        )
        strength_id = (
            request.env["dd.attribute.strength"]
            .sudo()
            .create(
                {
                    "strength_value": int(
                        post.get("character_attribute_strength_value", 0)
                    )
                }
            )
            .id
        )
        wisdom_id = (
            request.env["dd.attribute.wisdom"]
            .sudo()
            .create(
                {"wisdom_value": int(post.get("character_attribute_wisdom_value", 0))}
            )
            .id
        )

        vals = {
            "character_name": post.get("character_name"),
            "character_level": int(post.get("character_level", 0)),
            "character_stamina": int(post.get("character_stamina", 0)),
            "character_attribute_charisma": charisma_id,
            "character_attribute_constitution": constitution_id,
            "character_attribute_dexterity": dexterity_id,
            "character_attribute_intelligence": intelligence_id,
            "character_attribute_strength": strength_id,
            "character_attribute_wisdom": wisdom_id,
        }

        request.env["dd.character"].sudo().create(vals)
        return request.redirect("/list_characters")

    @http.route("/list_characters", type="http", auth="user", website=True)
    def list_characters(self, **kwargs):
        characters = request.env["dd.character"].sudo().search([])
        return request.render(
            "dd.dd_list_characters_template", {"characters": characters}
        )

    @http.route(["/save_dice_roll"], type="json", auth="public")
    def save_dice_roll(self, **kwargs):
        roll_result = kwargs.get("roll_result", 0)
        print(roll_result)
        # Faça algo com roll_result, como salvar em um modelo Odoo

    @http.route(
        "/character/<model('dd.character'):character>",
        type="http",
        auth="user",
        website=True,
    )
    def character(self, character, **kwargs):
        return request.render("dd.dd_character_template", {"character": character})
