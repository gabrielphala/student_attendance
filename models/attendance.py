from odoo import api, fields, models

class Attendance(models.Model):
	_name = "attendance.attendance"
	_description = "Student attendance records"
	name = fields.Char(string='name', required=True)
	student_id = fields.Many2one('attendance.student')
