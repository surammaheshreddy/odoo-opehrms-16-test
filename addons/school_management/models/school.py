from odoo import fields, api, models


class School(models.Model):
    _name  = 'school.student'
     
    Yourname = fields.Char(string='student',required = True,id='student')
    class_id = fields.Integer(string="class")
    department = fields.Char(string="Department")
    phonenum = fields.Integer(string="phonenum")