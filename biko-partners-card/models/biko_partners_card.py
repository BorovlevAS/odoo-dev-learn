# -*- coding: utf-8 -*-

from odoo import models, fields

class BikoPartnersCard(models.Model):
    _name = "biko.partners.card"
    _description = "BIKO partners card model"

    active = fields.Boolean('Active', readonly=True)
    name = fields.Char('Name', required = True, translate = True)
    address = fields.Char('Organization Address', required=False, translate=True)
    phone = fields.Char('Phone #')
    managerName = fields.Char('Manager''s name', required=False, translate=True)
    managerPhone = fields.Char('Manager''s phone')
    managerMail = fields.Char('Manager''s e-mail')

    ceoName = fields.Char('CEO name', required=False, translate=True)
    ceoPhone = fields.Char('CEO phone')
    ceoMail = fields.Char('CEO e-mail')

    partnerType = fields.Selection(
        string='Type',
        selection=[('start', 'New'), ('work', 'In progress'), ('stop', 'Wnd of work')],
        help="Type is used to separate partners")

