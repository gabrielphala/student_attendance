from odoo import api, fields, models

class Student(models.Model):
	_name = "attendance.student"
	_description = "Students records"
	name = fields.Char(string='name', required=True)
	student_no = fields.Char(string='Student no', required=True)
	email_address = fields.Char(string='Email address', required=True)
	gender = fields.Selection([('male','Male'), ('female', 'Female'), ('other', 'Other')], string='Gender', required=True)
