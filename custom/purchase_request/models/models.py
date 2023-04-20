# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class PurchaseRequest(models.Model):
    _name = "purchase.request"

    name = fields.Char(string="name", required=True, )
    user_id = fields.Many2one("res.user", required=1, default=lambda self: self.env.user, )
    date_start = fields.Date(string="Start Date", required=fields.Date.today)
    date_end = fields.Date(string="End Date")
    #reject_reason = fields.Text(string="Reject Reason", )
    reject_reason_ids = fields.One2many(comodel_name="create.rejection.wizard",
                                        inverse_name="wizard_reject_reason_id", string="Rejection Reason",)
    line_ids = fields.One2many("purchase.request.line", "purchase_request_id")
    total_cost = fields.Float(string="Total Price", required=True, compute="sum_totalcost",)

    state = fields.Selection([
        ("draft", "Draft"),
        ("to be approved", "To be Approved"),
        ("approve", "Approve"),
        ("reject", "Reject"),
        ("cancel", "Cancel"),
    ], default="draft", string="status")

    def action_to_be_approved(self):
        for rec in self:
            rec.state = 'to be approved'

    def cancel_button_test(self):
        for rec in self:
            rec.state = 'cancel'

    def action_approve(self):
        for rec in self:
            rec.state = 'approve'

    def action_reject(self):
        for rec in self:
            rec.state = 'reject'

    def action_reset_draft(self):
        for rec in self:
            rec.state = 'draft'





    @api.depends('line_ids')
    def sum_totalcost(self):
        for rec in self:
            total_cost = 0.0
            for line in rec.line_ids:
                total_cost += line.total
            rec.total_cost = total_cost

    def send_mail(self):
        self.env.ref("purchase_request.name_of_email_template").send_mail(self.id, email_values={
            'email_from':self.env.user.email,
            'email_to': "esraa@gmailcom",
        })









