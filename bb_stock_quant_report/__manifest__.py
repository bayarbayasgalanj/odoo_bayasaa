# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Stock Quant Report with Cost, Sale Price and Gross profit',
    'version': '1.0.1',
    'category': 'Stock',
    'icon': '/bb_stock_quant_report/static/description/icon.png',
    'sequence': 20,
    'author': 'Bayarbayasgalan MGL',
    'summary': 'Stock Extra tools',
    'description': """
This module can show Stock available quantity details with Cost and Sales Price
==============================================
If you want to show Stock Balance with cost and Sale.
You should take Stock Administrator at the user.
Cost is comfortable Average cost and Standard cost.
    """,
    'depends': ['stock','product'],
    'data': [
        'security/bb_stock_security.xml',
        'security/ir.model.access.csv',
        'views/stock_quant_view.xml',
        'views/stock_quant_report_view.xml',
    ],
    'qweb': [],
    'website': 'https://www.linkedin.com/in/bayarbayasgalan-jagdal/',
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
