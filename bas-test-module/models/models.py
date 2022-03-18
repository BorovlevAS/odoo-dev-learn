# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class bas-test-module(models.Model):
#     _name = 'bas-test-module.bas-test-module'
#     _description = 'bas-test-module.bas-test-module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
