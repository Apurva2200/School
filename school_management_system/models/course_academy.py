from odoo import api, fields, models


class CourseAcademy(models.Model):
    _name = "course.academy"
    _description = "Course Academy"

    name = fields.Char(string='Course Name', required=True)

    teacher_ids =fields.One2many('teacher.academy', 'teachers_course', string='Teacher_ids')
    student = fields.Many2many('student.academy',string='Student')








    # course_ref = fields.Many2one('teacher.academy', string='Course Ref')
#
# class CourseAcademyLine(models.Model):
#     _name = 'course.academy.line'
#     _description = "Course Academy Line"
#
#     course_id = fields.Many2one('course.academy', string='Course ID')
#     course_ref = fields.Many2one('teacher.academy', string='Teacher Assign')
#



