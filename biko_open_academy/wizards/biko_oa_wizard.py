from odoo import models, fields

class Biko_oa_wizard(models.TransientModel):
    _name = 'biko.oa.wizard'
    _description = 'BIKO: Open Academy Wizard'

    session_ids = fields.Many2many('biko.oa.sessions')
    attendee_ids = fields.Many2many('res.partner')

    def add_atteendees_to_sessions(self):
        for session in self.session_ids:
            session.attendee_id += self.attendee_ids
