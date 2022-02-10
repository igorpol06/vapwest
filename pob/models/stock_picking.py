#!/usr/bin/env python
# -*- coding: utf-8 -*-
##################################################################################
#                                                                                #
#    Copyright (c) 2016-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)#
#																				 #
##################################################################################

from odoo import api, fields, models, _
import logging
_logger = logging.getLogger(__name__)


class StockPicking(models.Model):
	_inherit = 'stock.picking'

	def action_sync_tracking_number(self):
		selected_ids = self._context.get('active_ids')
		if selected_ids:
			for k in self.env['stock.picking'].browse(selected_ids):
				tracking_data = k.get_tracking_data()
				sale_order_id = k.sale_id
				status = self.prestashop_sync_tracking_no(k, sale_order_id, tracking_data)
				if status:
					message = 'Tracking Number Succesfully Updated'
				else:
					message = "Some Issues While Updating Tracking Number To Prestashop"
		return self.env['message.wizard'].genrated_message(message)
	

	def prestashop_sync_tracking_no(self,pickingobj,sale_order,track_vals):
		status = False
		track_ref = track_vals.get('track_number','')
		sale_order_id = sale_order.id
		if sale_order_id and track_ref:
			check = self.env['connector.order.mapping'].search([('odoo_order_id', '=', sale_order_id)],limit=1)
			if check:
				instance_id = check.instance_id.id
				if instance_id:
					connection = self.env['connector.instance'].\
						with_context({'instance_id':instance_id})._create_prestashop_connection()
					prestashop = connection.get('prestashop', False)
					if prestashop:
						presta_id = check[0].ecommerce_order_id
						try:
							get_carrier_data = prestashop.get('order_carriers', options={'filter[id_order]':presta_id})
							order_carrier_id = get_carrier_data['order_carriers']['order_carrier']['attrs']['id']
							data = prestashop.get('order_carriers', order_carrier_id)
							data['order_carrier'].update({
										'tracking_number' : track_ref,
								})
							return_id = prestashop.edit('order_carriers', order_carrier_id, data)
							status = True
						except:
							pass
		return status


			