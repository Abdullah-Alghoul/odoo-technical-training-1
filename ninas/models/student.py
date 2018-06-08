# -*- coding: utf-8 -*-
# @author TK
# Date: 5/06/18

from odoo import fields, models, api
from odoo.exceptions import ValidationError, Warning


class Student(models.Model):
    _name = 'ninas.student'
    _description = 'Ninas Academy Student'
    _sql_constraints = [('student_uniq', 
                         'UNIQUE(name)', 
                         'Student ID must be unique!')]
    _inherit = 'mail.thread'

    name = fields.Char(
        string='Student ID', 
        required=False, 
        index=True)

    first_name = fields.Char(
        string='First Name', 
        required=True)

    last_name = fields.Char(
        string='Last Name', 
        required=True)

    email = fields.Char(
        string='Email')

    phone = fields.Char(
        string='Phone')

    age = fields.Selection(
        [(i, i) for i in range(100)],
        string='Age', 
        required=True)

    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female'), 
        ('transgender', 'Trangender'), ('other', 'Other')],
        required=True)

    level = fields.Selection(
        [('100', '100 Level'), ('200', '200 Level'),
        ('300', '300 Level'),('400', '400 Level')],
        required=True, 
        default='100')

    address = fields.Char(
        string='Address')

    city = fields.Char(
        string='City')

    state_id = fields.Many2one(
        comodel_name='res.country.state', 
        string='State')

    country_id = fields.Many2one(
        comodel_name='res.country', 
        string='Country')

    section_ids = fields.Many2many(
        comodel_name='ninas.section',
        compute='get_student_sections',
        string='Registered Sections')


    active = fields.Boolean(
        string='Active', default='t',
        groups='ninas.ninas_group_registrar')

    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Related Users')

    state = fields.Selection(
        [('new', 'New'), ('refused','Refused'), ('accepted','Accepted')],
        string='Status',
        default='new')


    @api.model
    def create(self, values):
        student = super(Student, self).create(values)
        student.name = student.create_student_id()
        if not self._context.get('copy_student', False):
            student.create_user()
        return student

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        self.ensure_one()
        self = self.with_context(copy_student=True)
        default = dict(default or {})
        default['name'] = False
        default['email'] = False
        default['user_id'] = False
        return super(Student, self).copy(default=default)

    @api.multi
    def write(self, values):
        country = self.env['res.country'].search([('code','=','NG')], limit=1)
        if country:
            values.update({'country_id':country.id})
        student = super(Student, self).write(values)
        if not self._context.get('copy_student', False):
            self.create_user()
        return student

    @api.multi
    def unlink(self):
        #students = self.filtered(lambda s: s.country_id.code != 'NG')   
        #return super(Student, self).unlink()
        return super(Student, self).write({'active':False})


    @api.multi
    def create_student_id(self):
        student = self.search([('id','!=',self.id),'|',('active','!=',False), ('active','=',False)], order='name DESC', limit=1)
        if student:
            previous_student_id = student.name
            return 'S'+ str(int(previous_student_id[1:])+1)
        return 'S1000001'



    @api.one
    def get_student_sections(self):
        section_obj = self.env['ninas.section']
        sections = section_obj.search([])

        section_ids = []
        for section in sections:
            for student in section.student_ids:
                if self.id == student.id:
                    section_ids.append(section.id)

        self.section_ids = [(6, 0, section_ids)]



    @api.constrains('email')
    def check_email(self):
        if self.email:
            students = self.search([('email', '=', self.email), ('id', '!=', self.id)])

            if students.ids:
                raise ValidationError('Email must be unique as Student ID: %s already uses this email'\
                    %(', '.join(map(str, students.mapped('name')))))



    @api.one
    def create_user(self):
        user_obj = self.env['res.users']
        values = {'name':self.first_name + ' '+self.last_name, 
                      'email':self.email,
                      'login':self.email,
                      'phone':self.phone}

        if self.user_id:
            self.user_id.update(values)
        else:
            user = user_obj.create(values)
            self.user_id = user.id


    def accept(self):
        if self.state in ['new', 'refused']:
            config = self.env['ninas.student.config'].search([], limit=1)
            mail_obj = self.env['mail.mail']
            if config.email_template_acceptance_id:
                values = config.email_template_acceptance_id.generate_email(self.id)
                mail = mail_obj.create(values)
                if mail:
                    mail.send()
                self.state = 'accepted'
            else:
                raise Warning('You must set acceptance email!')



class StudentConfig(models.Model):
    _name = 'ninas.student.config'
    _description = 'Ninas Student Configuration'

    
    email_template_refusal_id = fields.Many2one(
        comodel_name='mail.template',
        string='Refusal Email Template')

    email_template_acceptance_id = fields.Many2one(
        comodel_name='mail.template',
        string='Acceptance Email Template')
















