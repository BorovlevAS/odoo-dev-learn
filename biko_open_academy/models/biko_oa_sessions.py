from odoo import models, fields


class biko_oa_course(models.Model):
    _name = 'biko.oa.sessions'
    _description = 'BIKO: Open Academy. Sessions'

    name = fields.Char(required=True)
    startDate = fields.Date(required=True)
    duration = fields.Integer(required=True)
    seats = fields.Integer(required=True)
    course = fields.One2many('biko.oa.course', 'session_id')
    attendee_id = fields.Many2many('res.partner', 'attendee_id', string='Attendees list')