from odoo import models, fields, api
from datetime import date


class product_product(models.Model):
    _name = 'product_product_product'
    _description = 'products'

    name = fields.Char(string='Name')
    product_id = fields.Char(string='product ID')
    cost_price = fields.Float(string='Cost price')

    _sql_constraints = [
        ('id_product_unique', 'unique (product_id)', 'ID Has Been Takeen .'),
    ]
