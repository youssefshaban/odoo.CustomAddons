# -*- coding: utf-8 -*-

from odoo import models, fields


class school(models.Model):
    _name = 'school.school'
    _description = 'school.school'

    name = fields.Char(string="School name")
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
