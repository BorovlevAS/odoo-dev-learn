# -*- coding: utf-8 -*-

from odoo import models, fields


class biko_oa_course(models.Model):
    _name = 'biko.oa.course'
    _description = 'BIKO: Open Academy. Courses'

    active = fields.Boolean(default=True)
    name = fields.Char(required=True, string="Title")
    description = fields.Char()
    respUser = fields.Many2one('res.users')
    session_id = fields.One2many('biko.oa.sessions', 'course')

    _sql_constraints = [
        ('name_mustbe_uniq',
         "UNIQUE(name)",
         "You already have course with such name!")]

    def copy(self, default=None):
        new_name = 'Copy of ' + self.name
        default = dict(default or {}, name=new_name)
        return super(biko_oa_course, self).copy(default)
