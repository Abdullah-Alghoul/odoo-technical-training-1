# -*- coding: utf-8 -*-
# @author TK
# Date: 5/06/18

from odoo import http

class Section(http.Controller):

	@http.route('/ninas/sections', auth='public', website=True)
	def index(self, **kw):
		Sections = http.request.env['ninas.section']
		return http.request.render("ninas.index", {
			'sections':Sections.search([])
			})

	@http.route('/ninas/<name>/', auth='public', website=True)
	def section(self, name):
		return '<h1>{}</h1>'.format(name)

	"""	
	@http.route('/ninas/<int:id>/', auth='public', website=True)
	def count(self, id):
		return '<h1>{} ({})</h1>'.format(id, type(id).__name__)
	"""


	@http.route('/ninas/<model("ninas.section"):section>', auth='public', website=True)
	def get_section(self, section):
		return http.request.render('ninas.section', {
			'section': section
			})