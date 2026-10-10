from odoo import models, fields, api


class SchoolSubject(models.Model):
    _name = 'school.subject'
    _description = 'School Subject'

    name = fields.Char(string="Name")
    credit_hours = fields.Integer(string="Credit Hours")
    color = fields.Integer(string="Color")
    class_id = fields.Many2one('school.class', string="Class")
    academic_year_id = fields.Many2one(
        related='class_id.academic_year_id',
        string="Academic Year",
        store=True,
    )
