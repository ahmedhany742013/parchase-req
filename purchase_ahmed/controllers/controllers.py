# -*- coding: utf-8 -*-
from odoo import http


class PurchaseAhmed(http.Controller):
    @http.route('/purchase_ahmed/purchase_ahmed', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/purchase_ahmed/purchase_ahmed/objects', auth='public')
    def list(self, **kw):
        return http.request.render('purchase_ahmed.listing', {
            'root': '/purchase_ahmed/purchase_ahmed',
            'objects': http.request.env['purchase_ahmed.purchase_ahmed'].search([]),
        })

    @http.route('/purchase_ahmed/purchase_ahmed/objects/<model("purchase_ahmed.purchase_ahmed"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('purchase_ahmed.object', {
            'object': obj
        })
