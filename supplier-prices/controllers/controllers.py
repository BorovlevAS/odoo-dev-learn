# -*- coding: utf-8 -*-
# from odoo import http


# class Supplier-prices(http.Controller):
#     @http.route('/supplier-prices/supplier-prices', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/supplier-prices/supplier-prices/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('supplier-prices.listing', {
#             'root': '/supplier-prices/supplier-prices',
#             'objects': http.request.env['supplier-prices.supplier-prices'].search([]),
#         })

#     @http.route('/supplier-prices/supplier-prices/objects/<model("supplier-prices.supplier-prices"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('supplier-prices.object', {
#             'object': obj
#         })
