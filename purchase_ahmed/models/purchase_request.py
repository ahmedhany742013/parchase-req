
from odoo import models, fields, api



class PurchaseRequestWizard(models.TransientModel):
    _name = 'purchase.request.wizard'


    RejectionReason = fields.Text(string="Rejection Reason")


    def action_confirm_rejection(self):
        purch_req = self.env['purchase_ahmed.purchase_ahmed'].browse( self.env.context.get('active_id'))

        for rec in self:
          purch_req.RejectionReason = self.RejectionReason
          purch_req.state = 'Reject'


