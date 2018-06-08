# -*- coding: utf-8 -*-
# @author TK
# Date: 6/06/18

from odoo import fields, models, api

class Employee(models.Model):
    _inherit='hr.employee'

    is_instructor = fields.Boolean(
        string='Instructor?')

    section_ids = fields.One2many(
        comodel_name='ninas.section',
        inverse_name='instructor_id',
        string='Sections')