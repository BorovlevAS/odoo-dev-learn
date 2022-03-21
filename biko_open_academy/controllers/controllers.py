# -*- coding: utf-8 -*-
# from odoo import http


# class BikoOpenAcademy(http.Controller):
#     @http.route('/biko_open_academy/biko_open_academy', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/biko_open_academy/biko_open_academy/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('biko_open_academy.listing', {
#             'root': '/biko_open_academy/biko_open_academy',
#             'objects': http.request.env['biko_open_academy.biko_open_academy'].search([]),
#         })

#     @http.route('/biko_open_academy/biko_open_academy/objects/<model("biko_open_academy.biko_open_academy"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('biko_open_academy.object', {
#             'object': obj
#         })
