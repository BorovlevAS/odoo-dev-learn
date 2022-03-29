from odoo import models, fields

class Teachers(models.Model):

    _name = 'biko_academy.teachers'

    name = fields.Char(required=True)
    biography = fields.Html()
    course_ids = fields.One2many('biko_academy.courses', 'teacher_id', string='Courses')


class Courses(models.Model):
    _name = 'biko_academy.courses'
    _inherit = ['mail.thread', 'product.template']

    name = fields.Char(required=True)
    description = fields.Char()
    teacher_id = fields.Many2one('biko_academy.teachers', string="Teacher")
