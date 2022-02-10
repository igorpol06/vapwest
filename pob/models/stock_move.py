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


# Overriding this class in order to handle Stock Management b/w Odoo n PrestaShop.
class StockMove(models.Model):
	_inherit="stock.move"

	def prestashop_stock_update(self, erp_product_id, warehouse_id):
		return self.update_quantity_prestashop(erp_product_id,warehouse_id)
	
	def update_quantity_prestashop(self,erp_product_id, warehouse_id):
		ctx = self._context.copy() or {}
		product_pool = self.env['connector.product.mapping']
		check = product_pool.sudo().search([('name','=',erp_product_id)],limit=1)
		array = [0,'Error in Updating Stock']
		for map_obj in check:
			presta_product_id = map_obj.ecomm_id
			presta_product_attribute_id = map_obj.ecomm_combination_id
			instance_id = map_obj.instance_id
			if instance_id and warehouse_id == instance_id.warehouse_id.id:
				ctx.update({'instance_id':instance_id.id})
				connection = self.env['connector.instance'].sudo().with_context(ctx)._create_prestashop_connection()
				if connection['status'] and instance_id.inventory_sync == 'enable':
					ctx['warehouse'] = instance_id.warehouse_id.id
					product_qty = self.env['connector.snippet'].with_context(ctx) \
						.get_quantity(self.env['product.product'].browse(erp_product_id),instance_id.id)
					prestashop = connection.get('prestashop',False)
					if prestashop:
						try:
							stock_search = prestashop.get('stock_availables',
															options={'filter[id_product]':presta_product_id,
															'filter[id_product_attribute]':presta_product_attribute_id})
						except Exception as e:
							array.append([0,' Unable to search given stock id', erp_product_id])
							continue
						if type(stock_search['stock_availables']) == dict:
							if isinstance(stock_search['stock_availables']['stock_available'],list):
								stock_id = stock_search['stock_availables']['stock_available'][0]['attrs']['id']
							else:
								stock_id = stock_search['stock_availables']['stock_available']['attrs']['id']
							try:
								stock_data = prestashop.get('stock_availables', stock_id)
							except Exception as e:
								array.append([0,' Error in Updating Quantity,can`t get stock_available data.',erp_product_id])
							stock_data['stock_available']['quantity'] = int(product_qty)
							try:
								up = prestashop.edit('stock_availables', stock_id, stock_data)
							except:
								array.append([0,' Error in Updating Quantity,can`t get stock_available data.',erp_product_id])
							array.append([1,''])
				else:
					array.append([0 , 'Error in Connection with Prestashop',erp_product_id])
		return array
