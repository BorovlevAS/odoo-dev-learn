# -*- coding: utf-8 -*-

from odoo import models, fields

class BikoSoftWare(models.Model):
    _name = "biko.software"
    _description = "BIKO: software model"

    name = fields.Char('Name', required = True, translate = True)

