# -*- coding: utf-8 -*-
# @author TK
# Date: 4/06/18

from odoo import fields, models

class Course(models.Model):
    _name = 'ninas.course'
    _description = 'Ninas Academy Course'
    _inherit = 'mail.thread'

    name = fields.Char(
        string='Name', 
        required=True, 
        track_visibility='onchange')
    code = fields.Char(
        string='Code', 
        required=True,
        track_visibility='onchange')
    minimum_credit_hours = fields.Float(
        string='Minimum Credit Hours',
        digits=(2,2), 
        default=3.0,
        track_visibility='onchange')
    maximum_credit_hours = fields.Float(
        string='Maximum Credit Hours',
        digits=(2,2),
        default=3.0,
        track_visibility='onchange')
    description = fields.Text(
        string='Description',
        track_visibility='onchange')