# -*- coding: utf-8 -*-
from openerp import models, fields, api
import requests
import json
import logging

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def write(self, vals):
        res = super(SaleOrder, self).write(vals)
        if 'state' in vals:
            for order in self:
                # B2B'den gelen siparişleri ayırt etmek için client_order_ref kullanılır
                if order.client_order_ref:
                    self._sync_status_to_b2b(order, vals['state'])
        return res

    def _sync_status_to_b2b(self, order, odoo_state):
        # Statü Mapping: Onay:2, Teslim:5, İptal:8
        status_mapping = {
            'sale': 2,
            'sent': 5,
            'done': 5,
            'cancel': 8
        }
        
        target_status = status_mapping.get(odoo_state)
        if target_status:
            url = "https://connect.b2bstore.com/json/webservice.asmx/UpdateAllRows"
            guid = "CD052BC3-3EB8-4165-9A91-A8097BCFB183"
            
            data = [{
                "Trantype": "Order",
                "RowID": order.client_order_ref,
                "OrderStatusID": target_status,
                "OrderReferenceNo": order.name
            }]

            try:
                payload = {
                    "dbName": "",
                    "userName": guid,
                    "Password": "", 
                    "RowTemp": json.dumps(data)
                }
                requests.post(url, data=payload, timeout=10)
                _logger.info("B2BStore Sync: %s -> %s", order.name, target_status)
            except Exception as e:
                _logger.error("B2BStore Sync Error: %s", str(e))
        return True
