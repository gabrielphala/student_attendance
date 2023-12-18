from odoo import api, fields, models

class Student(models.Model):
	_name = "attendance.student"
	_description = "Students records"
	name = fields.Char(string='name', required=True)
	student_no = fields.Integer(string='Student no')
	email_address = fields.Text(string='Email address')
	gender = fields.Selection([('male','Male'), ('female', 'Female'), ('other', 'Other')], string='Gender')
