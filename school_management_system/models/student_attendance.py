from odoo import fields, models, api


class StudentAttendance(models.Models):
    _name = 'student.attendance'
    _description = 'Student Attendance'

    student_id = fields.Many2one('student.student', string="Student")