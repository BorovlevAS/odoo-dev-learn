# -*- coding: utf-8 -*-
# from odoo import http


# class Bas-test-module(http.Controller):
#     @http.route('/bas-test-module/bas-test-module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bas-test-module/bas-test-module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bas-test-module.listing', {
#             'root': '/bas-test-module/bas-test-module',
#             'objects': http.request.env['bas-test-module.bas-test-module'].search([]),
#         })

#     @http.route('/bas-test-module/bas-test-module/objects/<model("bas-test-module.bas-test-module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bas-test-module.object', {
#             'object': obj
#         })
