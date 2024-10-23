from odoo import api, fields, models
from datetime import date


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Record'
   
    name = fields.Char(string='Name', required=True)
    date_of_birth = fields.Date(string='Date of Birth')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    age = fields.Integer(string='Age', compute='_compute_age')
    phone = fields.Char(string='Phone')

    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            if record.date_of_birth:
                record.age = date.today().year - record.date_of_birth.year
            else:
                record.age = 0
