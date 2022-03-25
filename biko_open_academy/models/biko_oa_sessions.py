from odoo import models, fields, api
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError


class biko_oa_sessions(models.Model):
    _name = 'biko.oa.sessions'
    _description = 'BIKO: Open Academy. Sessions'

    active = fields.Boolean(default=True)
    name = fields.Char(required=True)

    start_date = fields.Date(default=datetime.today(), required=True)
    duration = fields.Integer(required=True)
    end_date = fields.Date(compute='_compute_end_date', store=True)

    seats = fields.Integer(required=True)
    taken_seats = fields.Float(compute='_compute_taken_seats')

    course = fields.Many2one('biko.oa.course', required=True)
    instructor = fields.Many2one('res.partner',
                                 domain="['|', ('teacher', '=', 'teacher_level1'), "
                                        "'|', ('teacher', '=', 'teacher_level2'), "
                                        "('instructor', '=', 'True')]")
    attendee_id = fields.Many2many('res.partner', column1 ='attendee_id', column2 ='partner_id', string='Attendees list')
    attendees_count = fields.Integer(compute='_compute_attendees', store=True)

    @api.depends('start_date', 'duration')
    def _compute_end_date(self):
        for rec in self:
            rec.end_date = rec.start_date + timedelta(days=rec.duration)

    @api.depends('attendee_id', 'seats')
    def _compute_taken_seats(self):
        for record in self:
            if not record.seats:
                record.taken_seats = 0
            else:
                record.taken_seats = 100 * len(record.attendee_id) / record.seats

    @api.onchange('seats')
    def _onchange_seats(self):
        for r in self:
            if r.seats < 0:
                raise ValidationError("You can't set negative number of seats")

    @api.depends('attendee_id')
    def _compute_attendees(self):
        for r in self:
            r.attendees_count = len(r.attendee_id)

    @api.constrains('instructor', 'attendee_id')
    def _check_instructor_not_attendee(self):
        for r in self:
            if r.seats < len(r.attendee_id):
                raise ValidationError('There are only %s seats can be taken!' % r.seats)
            if r.instructor and r.instructor in r.attendee_id:
                raise ValidationError("Instructor or teqcher %s can't be attendee!" % r.instructor.name)
