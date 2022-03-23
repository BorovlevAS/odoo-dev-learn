# -*- coding: utf-8 -*-

from odoo import models, fields


class biko_oa_course(models.Model):
    _name = 'biko.oa.course'
    _description = 'BIKO: Open Academy. Courses'

    active = fields.Boolean(default=True)
    name = fields.Char(required=True, string="Title")
    description = fields.Char()
    respUser = fields.Many2one('res.users')
    instructor = fields.Many2one('res.partner')
    session_id = fields.Many2one('biko.oa.sessions', required=True)
