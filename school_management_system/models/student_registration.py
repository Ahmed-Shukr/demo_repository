from datetime import date

from odoo import api, fields, models

from .school_academic_year import default_academic_year


class StudentRegistration(models.Model):
    _name = "student.student"
    _description = "Student Registration"

    name = fields.Char(string="Student Name")
    sequence = fields.Integer(string="Sequence")
    registration_no = fields.Char(string="Student ID")
    age = fields.Integer(string="Age", compute="_compute_age", inverse="_inverse_age", store=True)
    birth_date = fields.Date(string="Birth Date")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    address = fields.Char(string="Address")
    is_graduated = fields.Boolean(string="Is Graduated", default=False)
    is_scholarship = fields.Boolean(string="Is Scholarship", default=False)
    academic_year_id = fields.Many2one(
        'school.academic.year',
        string="Academic Year",
        default=default_academic_year,
    )
    class_id = fields.Many2one('school.class', string="Class Name", ondelete="cascade")
    currency_id = fields.Many2one(comodel_name='res.currency', string="Currency", default=1)
    tuition_fee = fields.Monetary(related="class_id.tuition_fee", string="Tuition Fee", currency_field="currency_id", store=True)
    school_subject_ids = fields.Many2many('school.subject', string="School Subjects")
    supervisor = fields.Char(related="class_id.department_id.manager_id.name")
    remarks = fields.Text(string="Remarks")
    admission_date = fields.Datetime(string="Admission Date", default=fields.Datetime.now)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    nationality = fields.Many2one('res.country', 'Nationality')
    blood_group = fields.Selection([
        ('A+', 'A+ve'),
        ('B+', 'B+ve'),
        ('O+', 'O+ve'),
        ('AB+', 'AB+ve'),
        ('A-', 'A-ve'),
        ('B-', 'B-ve'),
        ('O-', 'O-ve'),
        ('AB-', 'AB-ve')
    ], string='Blood Group')
    secondary_school = fields.Many2one('school.school', string="Secondary School")
    school_location = fields.Char(string="School Location")
    average_marks = fields.Float(string="Average Marks", default=60.0)
    secondary_certificate = fields.Binary('Secondary Certificate')
    image = fields.Binary(string="Image")
    transport_required = fields.Boolean(string="Transport Required")
    number_of_seats = fields.Integer(string="No of Seats", related="class_id.no_of_seats")
    status = fields.Selection(
        [('new', 'New'), ('enrolled', 'Enrolled'), ('drop_out', 'Drop Out'), ('graduated', 'Graduated')],
        string="Status", default='new')
    teacher_subject_id = fields.Reference([('school.teacher', 'Teachers'), ('school.subject', 'Subjects')],
                                          string="Teachers & Subjects")
    active = fields.Boolean(string="Active", default=True)

    @api.depends('birth_date')
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                today = date.today()
                record.age = (
                        today.year - record.birth_date.year)
            else:
                record.age = 0


    def _inverse_age(self):
        for record in self:
            if record.age:
                record.birth_date = (
                    date.today().replace(
                        year=date.today().year - record.age
                    )
                )


    @api.onchange('gender','registration_no')
    def _onchange_gender(self):
        self.average_marks = 90

    @api.onchange('class_id')
    def _onchange_class_academic_year(self):
        if self.class_id.academic_year_id:
            self.academic_year_id = self.class_id.academic_year_id

    @api.onchange('academic_year_id')
    def _onchange_academic_year(self):
        if self.class_id and self.academic_year_id and self.class_id.academic_year_id != self.academic_year_id:
            self.class_id = False


