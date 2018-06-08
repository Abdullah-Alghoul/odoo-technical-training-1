# -*- coding: utf-8 -*-
# @author TK
# Date: 4/06/18
"""
field name, operator, value

[('field_name', 'operator', 'value')]

 field_name = 'any field that exist on that model'
 operator  = '> < <= >= =', 'in ilike like =ilike not'

 value = 'integer, float, datetime, list many2one [id], one2many [ids], many2many [ids], boolean'

 section_obj = self.env['ninas.section']

 section_obj.create(values- dict)
 section_obj.write(values - dict) / section_obj.update(values - dict)
 section_obj.search(domain - list) eg section_obj.search(['&', '|', ('id','=',1), ('name','=','a'), ('course_id','=',1)])
 object.unlink()

 section_obj.browse([1,2])                                     
"""
from odoo import fields, models, api
import datetime

class Section(models.Model):
    _name = 'ninas.section'
    _description = 'Ninas Academy Sections'
    _order = 'name DESC'

    _sql_constraints = [('section_uniq', 
                         'UNIQUE(name)', 
                         'Section name must be unique!')]

    name = fields.Char(
        string='Name', 
        required=False, 
        readonly=False)
    course_id = fields.Many2one(
        comodel_name='ninas.course',
        string='Course', 
        required=True
        )

    code = fields.Char(
        related='course_id.code',
        store=True)

    credit_hours = fields.Float(
        string='Credit Hours', 
        digits=(2,2))
    start_time = fields.Float(
        string='Start Time')
    end_time = fields.Float(
        string='End Time')

    start_date = fields.Date(
        string='Start Date')

    end_date = fields.Date(
        string='End Date')

    number_of_students = fields.Integer(
        string='Number of Students', 
        compute='calculate_number_of_students',
        store=False)

    student_ids = fields.Many2many(
        comodel_name='ninas.student',
        relation='ninas_student_section_rel',
        column1='section_id',
        column2='student_id',
        string='Students')

    instructor_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Instructor')



    """@api.model
    def create(self, values):
        section = super(Section, self).create(values)
        section.name = section.compute_section_name()
        return section
    """

    """def write(self, values):
        return

    def unlink(self):
        return
    """

    @api.onchange('student_ids')
    @api.multi
    def calculate_number_of_students(self):
        for section in self:
            section.number_of_students = len(section.student_ids.ids)



    @api.onchange('course_id')
    def compute_section_name(self):
        year = datetime.date.today().year
        section_obj = self.env['ninas.section']
        course_code = self.course_id.code or ''
        no_of_sections = 100
        sections = section_obj.search(
            [('course_id','=',self.course_id.id)])
        if sections.ids:
            no_of_sections += len(sections.ids)

        self.name = str(year)+course_code+str(no_of_sections)

