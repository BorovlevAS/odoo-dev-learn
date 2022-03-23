from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError


class biko_oa_sessions(models.Model):
    _name = 'biko.oa.sessions'
    _description = 'BIKO: Open Academy. Sessions'

    active = fields.Boolean(default=True)
    name = fields.Char(required=True)
    start_date = fields.Date(default=datetime.today(), required=True)
    duration = fields.Integer(required=True)
    seats = fields.Integer(required=True)
    percents = fields.Float('% of taken seats', compute='_compute_percents', digits=(5, 3))
    course = fields.One2many('biko.oa.course', 'session_id')
    instructor = fields.Many2one('res.partner',
                                 domain="['|', ('teacher', '=', 'teacher_level1'), "
                                        "'|', ('teacher', '=', 'teacher_level2'), "
                                        "('instructor', '=', 'True')]")
    attendee_id = fields.Many2many('res.partner', column1 = 'attendee_id', column2 = 'partner_id', string='Attendees list')

    def _compute_percent_record(record):
        if (record.seats == 0):
            record.percents = 0
        else:
            record.percents = len(record.attendee_id) * 100 / record.seats

    @api.depends('attendee_id', 'seats')
    def _compute_percents(self):
        if len(self) == 1:
            biko_oa_sessions._compute_percent_record(self)
        else:
            for record in self:
                biko_oa_sessions._compute_percent_record(record)


    @api.onchange('seats')
    def _onchange_seats(self):
        if self.seats < 0:
            raise ValidationError("You can't set negative number of seats")

    @api.onchange('attendee_id')
    def _onchange_attendees(self):
        if self.seats < len(self.attendee_id):
            raise ValidationError('There are only %s seats can be taken!' % self.seats)

        for rec in self.attendee_id:
            if rec.instructor:
                raise ValidationError("Instructor %s can't be attendee!" % rec.name)
