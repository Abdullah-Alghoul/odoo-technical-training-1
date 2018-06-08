# -*- coding: utf-8 -*-
# @author TK
# Date: 5/06/18

from odoo import fields, models, api


class Instructor(models.Model):
	_name = 'ninas.instructor'
	_inherit = 'hr.employee'