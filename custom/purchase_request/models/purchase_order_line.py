# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class PurchaseOrderLine(models.Model):
    # inherit from purchase.order.line
    _inherit = 'purchase.order.line'

    # check quantity of purchase order line  and raise error if  quantity of purchase order line exceeds
    # the quantity in the purchase request line

    @api.constrains("product_qty")
    def check_quantity(self):
        for purchase_line in self:
            purchase_request_lines = self.env['purchase.request.line'].search([
                ('product_id', '=', purchase_line.product_id.id),
                ('purchase_request_id', '=', purchase_line.order_id.request_id.id),
            ])
            for request_line in purchase_request_lines:
                if purchase_line.product_qty > request_line.quantity:
                    raise UserError(_('The quantity in the purchase order line exceeds'
                                    ' the quantity in the purchase request line.'))

