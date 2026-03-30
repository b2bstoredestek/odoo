# -*- coding: utf-8 -*-
{
    'name': 'B2BStore Odoo 8.0 Connector',
    'version': '1.0',
    'author': 'B2BStore Destek',
    'category': 'Sales',
    'summary': 'B2BStore Sipariş ve Statü Senkronizasyonu',
    'description': """
B2BStore Platformu ile Odoo 8.0 Arasında Tam Entegrasyon Sağlar.
---------------------------------------------------------------
* B2B'den gelen onaylı siparişleri Odoo'ya aktarır.
* Odoo statü değişikliklerini B2B'ye iletir (Onay: 2, İptal: 8, Teslim: 5).
    """,
    'depends': ['sale'],
    'data': [
        'views/sale_order_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
