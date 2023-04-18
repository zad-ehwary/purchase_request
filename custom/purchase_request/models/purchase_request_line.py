# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseRequestLine(models.Model):
    _name = "purchase.request.line"

    cost_price = fields.Float(string="Cost Price", readonly=1, related="product_id.standard_price")

    # total = fields.Float(string="Total", readonly=1, compute="_get_price_total")
    total = fields.Float(string="Total", readonly=1, compute="_get_price_total")

    purchase_request_id = fields.Many2one("purchase.request")

    product_id = fields.Many2one(comodel_name="product.product", string="Product ID", required=True)
    description = fields.Char(string="Description", related="product_id.name")

    quantity = fields.Float(string="Quantity", default=1)

    @api.depends("quantity", "cost_price")
    def _get_price_total(self):
        for rec in self:
            rec.total= rec.quantity * rec.cost_price