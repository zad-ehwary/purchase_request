# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CreateRejectionWizard(models.TransientModel):
    _name = "create.rejection.wizard"
    
    
    wizard_reject_reason = fields.Text(string="Reject Reason", )
    wizard_reject_reason_id = fields.Many2one(comodel_name="purchase.request", string="Rejection Reason id ", required=False, )

    def submit_button(self):
        # Get the active purchase request
        parent_purchaes_request = self.env['purchase.request'].browse(self.env.context.get('active_id'))
        reasons = self.env["create.rejection.wizard"].create({
            "wizard_reject_reason_id": parent_purchaes_request.id,
            "wizard_reject_reason": self.wizard_reject_reason

        })


        return {'type': 'ir.actions.act_window',
                "res_model" : "purchase.request",
                "res_id" : parent_purchaes_request.id,
                "view_mode" :"form",
                "target": "main"


                }



