from odoo import models, fields

class BikoOAWizard(models.TransientModel):
    _name = 'biko.oa.wizard'
    _description = 'BIKO: Open Academy Wizard'

    session_ids = fields.Many2many('biko.oa.session')
    attendee_ids = fields.Many2many('res.partner')

    def add_attendees_to_sessions(self):
        for session in self.session_ids:
            for x in self.attendee_ids:
                session.attendee_id = [(4, x.id)]
