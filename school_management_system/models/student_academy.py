from odoo import api, fields, models


class StudentAcademy(models.Model):
    _name = "student.academy"
    _description = "Student Academy"

    roll_no = fields.Char(string='Roll_no', required=True)
    name = fields.Char(string='Name', required=True)
    image = fields.Binary(string="student image")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male')
    date_of_birth = fields.Datetime(string='date_of_birth')
    e_mail = fields.Char(string='E_mail', required=True)
    mobile = fields.Char(string='Mobile', required=True)


    #each student enroll only one course

    enrolled_course = fields.Many2one('course.academy', string='Enrolled Course')

    #multiple course for multiple student

    another_course = fields.Many2many('course.academy', string='Another Course')


    @api.constrains('enrolled_course')
    def _check_unique_course_enrollment(self):
        for student in self:
            if student.enrolled_course and self.search_count([('enrolled_course', '=', student.enrolled_course.id)]) > 1:
                raise ValidationError("Each student can be enrolled in only one course!")