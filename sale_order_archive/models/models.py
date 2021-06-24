# -*- coding: utf-8 -*-
import datetime
from odoo import models, fields, api


class SaleOrderArchive(models.Model):
    """Model for archived sale.order"""
    _name = 'sale.order.archive'

    name = fields.Char()
    order_create_date = fields.Datetime(string='Order create date')
    customer = fields.Many2one('res.partner')
    sale_person = fields.Many2one('res.user', string='Sale Person')
    order_currency = fields.Many2one('res.currency', string='Order Currency')
    order_total_amount = fields.Monetary(string='Order Total Amount', currency_field='order_currency')
    count_of_order_lines = fields.Integer(string='Count of Order Lines')

    @api.model
    def _archiving_sale_orders(self) -> None:
        """Archiving an sale.order if the sale.order was created 7 days ago and removing this sale.order"""
        archive_date_from = datetime.datetime.now() - datetime.timedelta(days=7)
        orders_to_archive = self.env['sale.order'].search([('create_date', '<', archive_date_from)])
        if orders_to_archive:
            for order in orders_to_archive.search([]):
                lines = len(self.env['sale.order.line'].search([('order_id', '=', order['id'])]))
                archive_order = {
                    'name': order['display_name'],
                    'order_create_date': order['create_date'],
                    'customer': order['partner_id'].id,
                    'sale_person': order['activity_user_id'].id,
                    'order_total_amount': order['amount_total'],
                    'order_currency': order['currency_id'].id,
                    'count_of_order_lines': lines,
                }
                self.env['sale.order.archive'].create(archive_order)
            orders_to_archive.unlink()
