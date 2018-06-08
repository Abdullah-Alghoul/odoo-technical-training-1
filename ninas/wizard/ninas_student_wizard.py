# -*- coding: utf-8 -*-
# @author TK
# Date: 8/06/18


from odoo import fields, models, api

import logging


logger = logging.getLogger(__name__)


class NinasStudentWizard(models.TransientModel):
    _name = 'ninas.student.wizard'
    _description = 'Ninas Academy Student Wizard'

    section_ids = fields.Many2many(
        comodel_name='ninas.section',
        relation='ninas_section_wizard_rel',
        column1='student_id',
        column2='section_id',
        string='Sections', 
        required=True)


    def join_sections(self):

        """
        logger.info()
        logger.warning()
        logger.debug()
        logger.error()
        """
        student_id = self._context.get('active_id')
        logger.info('Student ID: %s' %student_id)

        self.section_ids.write({'student_ids':[(4, student_id)]})

        return

