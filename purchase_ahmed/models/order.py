from odoo import models, fields, api


class order_r(models.Model):
    _name = 'order.rrr'
    _description = 'order'

    product_id = fields.Many2one("product_product_product", required=1)

    Description = fields.Char(string='Description', compute='_Product_name')
    Quantity = fields.Float(string='Quantity', default='1')
    CostPrice = fields.Float(string="Cost Price", readonly=1, compute='_Product_name')
    Total = fields.Monetary(string='Total', compute='_total')
    order_liness = fields.Many2one('purchase_ahmed.purchase_ahmed')
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id')
    company_id = fields.Many2one('res.company', related='order_liness.RequestedBy_id.company_id')

    @api.depends('product_id', 'Description', 'CostPrice')
    def _Product_name(product_id):
        for rec in product_id:
            if rec.product_id.name and rec.product_id.cost_price:
                rec.Description = rec.product_id.name
                rec.CostPrice = rec.product_id.cost_price
            else:
                rec.Description = ' '
                rec.CostPrice =''


    @api.depends('CostPrice','Quantity')
    def _total(self):
       for rec in self:
        if rec.CostPrice and rec.Quantity:
            rec.Total = rec.CostPrice * rec.Quantity
        else:
            rec.Total = '0'
