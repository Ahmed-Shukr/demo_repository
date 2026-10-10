from odoo import api, fields, models

from .school_academic_year import default_academic_year


class SchoolTeacher(models.Model):
    _name = 'school.teacher'
    _description = 'School Teacher'

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    address = fields.Char(string="Address")
    weekly_hours = fields.Float(string="Weekly Hours")
    signature = fields.Binary(string="Signature")

    # Relationships
    academic_year_id = fields.Many2one(
        'school.academic.year',
        string="Academic Year",
        default=default_academic_year,
    )
    class_id = fields.Many2many('school.class', string="Class/Classes")
    tags = fields.Many2many('school.teacher.tag', string="Tags")

    # Rating selection
    teacher_rating = fields.Selection([
        ('0', 'Ineffective'),
        ('1', 'Developing'),
        ('2', 'Effective'),
        ('3', 'Highly Effective')
    ], string="Teacher Rating", default='2')



class SchoolTeacherTag(models.Model):
    _name = 'school.teacher.tag'
    _description = 'Teacher Tag'

    name = fields.Char(string="Tag Name", required=True)
    color = fields.Integer(string="Color Index")  # Odoo uses integers (0-11) for badge colors
