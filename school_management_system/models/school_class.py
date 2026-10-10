from odoo import fields, models, api

from .school_academic_year import default_academic_year


class SchoolClass(models.Model):
    _name = 'school.class'
    _description = 'School Class'

    name = fields.Char(string='Class Name')
    academic_year_id = fields.Many2one(
        'school.academic.year',
        string="Academic Year",
        default=default_academic_year,
    )
    class_description = fields.Html(string="Class Description")
    code = fields.Text(string="Coding")
    currency_id = fields.Many2one(comodel_name='res.currency', string="Currency", default=1)
    tuition_fee = fields.Monetary(string="Tuition Fee", currency_field="currency_id")
    no_of_seats = fields.Integer(string="No of Seats")
    student_ids = fields.One2many(comodel_name='student.student', inverse_name='class_id', string="Students")
    student_count = fields.Integer(string="Students", compute="_compute_student_count")
    department_id = fields.Many2one(comodel_name='hr.department', string="Department")

    @api.depends('student_ids')
    def _compute_student_count(self):
        for record in self:
            record.student_count = len(record.student_ids)

    def action_view_students(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Students',
            'res_model': 'student.student',
            'view_mode': 'list,form',
            'domain': [('class_id', '=', self.id)],
            'context': {'default_class_id': self.id},
        }

