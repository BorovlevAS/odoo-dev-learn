from odoo import models, fields

class Partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    instructor = fields.Boolean()
    teacher = fields.Selection([('teacher_level1', "Teacher / Level 1"), ('teacher_level2', "Teacher / Level 2")])
    session_ids = fields.Many2many('biko.oa.sessions', column1 = 'partner_id', column2 = 'attendee_id')
