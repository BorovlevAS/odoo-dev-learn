# -*- coding: utf-8 -*-
# from odoo import http


# class Bas-real-estate(http.Controller):
#     @http.route('/bas-real-estate/bas-real-estate', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bas-real-estate/bas-real-estate/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bas-real-estate.listing', {
#             'root': '/bas-real-estate/bas-real-estate',
#             'objects': http.request.env['bas-real-estate.bas-real-estate'].search([]),
#         })

#     @http.route('/bas-real-estate/bas-real-estate/objects/<model("bas-real-estate.bas-real-estate"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bas-real-estate.object', {
#             'object': obj
#         })
