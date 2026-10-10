from odoo import api, fields, models
from odoo.exceptions import ValidationError


def default_academic_year(self):
    today = fields.Date.context_today(self)
    return self.env['school.academic.year'].search([
        ('date_start', '<=', today),
        ('date_end', '>=', today),
    ], limit=1)


class SchoolAcademicYear(models.Model):
    _name = 'school.academic.year'
    _description = 'Academic Year'
    _order = 'date_start desc, name'

    name = fields.Char(string="Academic Year", required=True)
    date_start = fields.Date(string="Start Date", required=True)
    date_end = fields.Date(string="End Date", required=True)
    active = fields.Boolean(string="Active", default=True)

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Academic Year must be unique.'),
    ]

    @api.constrains('date_start', 'date_end')
    def _check_dates(self):
        for record in self:
            if record.date_start and record.date_end and record.date_start > record.date_end:
                raise ValidationError("Start Date must be before End Date.")
