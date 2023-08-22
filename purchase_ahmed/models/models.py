from odoo import models, fields, api
from datetime import date


class purchase_ahmed(models.Model):
    _name = 'purchase_ahmed.purchase_ahmed'
    _description = 'purchase_ahmed.purchase_ahmed'

    Request_name = fields.Char(string='Request name', required='true')
    RequestedBy_id = fields.Many2one('res.users', string='RequestedBy', defoult='Active user')
    StartDate = fields.Date(string="Start Date", default=date.today())
    EndDate = fields.Date(string="End Date")
    RejectionReason = fields.Text(string="Rejection Reason", readonly='1')
    orderlines = fields.One2many('order.rrr', 'order_liness', string='orderlines')
    TotalPrice = fields.Monetary(currency_field='currency_id', string="TotalPrice", compute='_total')
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id')
    company_id = fields.Many2one('res.company', related='RequestedBy_id.company_id')
    state = fields.Selection(
        [('draft', 'Draft'), ('to be approved', 'To be approved'), ('approve', 'Approve'), ('Reject', 'reject'),
         ('Cancel', 'cancel')], string='Status', default='draft', readonly='true')

    @api.depends('orderlines')
    def _total(self):
        for rec in self:
            total = 0
            for line in rec.orderlines:
                if line.Total:
                    total += line.Total
            rec.TotalPrice = total

    def Submit_for_Approval(self):
        for rec in self:
            rec.state = 'to be approved'

    def cancel(self):
        for rec in self:
            rec.state = 'Cancel'

    def send_email_templete(self):
     templat= self.env.ref('purchase.email_template_edi_purchase_reminder')
     for rec in self:
       templat.send_mail(rec.RequestedBy_id.id ,force_send='true')
       rec.state = "approve"

    def draft(self):
        for rec in self:
            rec.state = "draft"

    def reset(self):
        for rec in self:
            rec.state = "draft"


    def button_create_PO(self):
        orders_line = []
        for line in self.line_ids:
            orders_line.append((0, 0,
                                {'name': line.product_id.display_name,
                                 'product_qty': line.qty,
                                 'product_id': line.product_id.id,
                                 'price_unit': line.cost_price,
                                 }

                                ))

        purchase_order = self.env['purchase.order'].create(
            {
                'partner_id': self.partner_id.id,
                'order_line': orders_line,
                'name_id': self.id,
            }
        )

        return {
            'name': _('Create purchase.order'),
            'type': 'ir.actions.act_window',
            'res_model': 'purchase.order',
            'view_type': 'form',
            'view_mode': 'form',
            'domain': [('name_id', '=', self.id)],
            'res_id': purchase_order.id,

        }

    def action_view_order(self):
        return


    @api.depends('name')
    def compute_order_count(self):
        for record in self:
            num_orders = self.env['purchase.order'].search_count([('name_id', '=', record.id)])
            record.num_orders = num_orders