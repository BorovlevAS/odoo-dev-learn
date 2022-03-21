# -*- coding: utf-8 -*-

from odoo import models, fields


class biko_oa_course(models.Model):
    _name = 'biko.oa.course'
    _description = 'BIKO: Open Academy. Courses'

    title = fields.Char(required=True)
    description = fields.Char()
