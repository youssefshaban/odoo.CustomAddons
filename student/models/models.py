# -*- coding: utf-8 -*-

from odoo import models, fields


class student(models.Model):
    _name = 'school.student'
    _description = 'school.student'

    name = fields.Char()
    school_id = fields.Many2one("school.school",string="School name")
    hobbies_list = fields.("hobbies","school_hobby_rel","student_id","hobbies_id",string="hobbies")



class SchoolProfile(models.Model):
    _inherit = "school.school"

    school_list = fields.One2many("school.student","school_id",string="students list")

class Hobbies(models.Model):
    _name = 'hobbies'
    name = fields.Char(string="Hobbies")
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
