from odoo import api, fields, models


class TeacherAcademy(models.Model):
    _name = "teacher.academy"
    _description = "Teacher Academy"

    name = fields.Char(string='Name', required=True)
    # course = fields.Char(string="Course", required=True)
    image = fields.Binary(string="student image")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male')


    #each teacher is associated with only one course.
    
    teachers_course = fields.Many2one('course.academy', string='Teacher Course')



    @api.constrains('teacher_course')
    def _check_unique_course_enrollment(self):
        for teacher in self:
            if teacher.teachers_course and self.search_count([('teachers_course', '=', teacher.teachers_course.id)]) > 1:
                raise ValidationError("Each Teacher is assosiated with only one course!")

