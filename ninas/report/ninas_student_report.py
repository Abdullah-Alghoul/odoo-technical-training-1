# -*- coding: utf-8 -*-
# @author TK
# Date: 9/06/18

from odoo import models, api


class StudentReport(models.Model):
    _name = 'report.ninas.ninas_student_report'
    _description = 'Ninas Academy Student Report'


    def _get_sections(self, student_ids):
        """

            for section in sections:
                for section_student in section.student_ids:
                    if section_student.id == student.id:

                        student_sections[student.id].append({
                            'name': section.name,
                            'course_name': section.course_id.name,
                            'course_code': section.code
                            })
                        break
        """

        section_obj = self.env['ninas.section']
        sections = section_obj.browse([19])
        students = self.env['ninas.student'].browse(student_ids)
        student_sections = {}

        for student in students:
            for section in sections:
                for section_student in section.student_ids:
                    if section_student.id == student.id:
                        student_sections[student.id].append({
                            'name': section.name,
                            'course_name': section.course_id.name,
                            'course_code': section.code
                            })
                        break

        return student_sections




    @api.model
    def get_report_values(self, docids, data=None):
        students = self.env['ninas.student'].browse(docids)


        return {
            'doc_ids': docids,
            'doc_model': 'ninas.student',
            'docs': students,
            'data': data,
            'get_sections': self._get_sections(students.ids),
        }



