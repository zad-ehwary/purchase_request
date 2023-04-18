# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CreateRejectionWizard(models.TransientModel):
    _name = "create.rejection.wizard"

    #reject_reason = fields.Text(string="Reject Reason", )
    reject_reason_id = fields.Many2one(comodel_name="purchase.request", string="Rejection Reason", required=True, )

    def action_confirm(self):
        # Get the active purchase request
        request = self.env['purchase.request'].browse(self.env.context.get('active_id'))

        # Set the rejection reason and reject the purchase request
        request.write({'reject_reason_id': self.reject_reason_ids, 'state': 'reject'})
        request.button_reject()

        return {'type': 'ir.actions.act_window_close'}




