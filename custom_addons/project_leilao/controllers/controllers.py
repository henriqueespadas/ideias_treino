# -*- coding: utf-8 -*-
# from odoo import http


# class ProjectLeilao(http.Controller):
#     @http.route('/project_leilao/project_leilao/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_leilao/project_leilao/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_leilao.listing', {
#             'root': '/project_leilao/project_leilao',
#             'objects': http.request.env['project_leilao.project_leilao'].search([]),
#         })

#     @http.route('/project_leilao/project_leilao/objects/<model("project_leilao.project_leilao"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_leilao.object', {
#             'object': obj
#         })
