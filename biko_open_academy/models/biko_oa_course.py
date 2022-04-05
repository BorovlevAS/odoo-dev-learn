from odoo import models, fields

class Course(models.Model):
    _name = 'biko.oa.course'
    _description = 'BIKO: Open Academy. Course'

    active = fields.Boolean(default=True)
    name = fields.Char(required=True, string="Title")
    description = fields.Char()
    resp_user_id = fields.Many2one('res.users')
    session_ids = fields.One2many('biko.oa.session', 'course')

    _sql_constraints = [
        ('name_mustbe_uniq',
         "UNIQUE(name)",
         "You already have course with such name!")]

    def copy(self, default=None):
        new_name = 'Copy of ' + self.name
        default = dict(default or {}, name=new_name)
        return super(Course, self).copy(default)

