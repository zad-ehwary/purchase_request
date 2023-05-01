# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Purchase_order(models.Model):
    _name = 'purchase.order'
    _inherit = 'purchase.order'

    request_id = fields.Many2one(comodel_name="purchase.request", string="request_id", required=False, )




