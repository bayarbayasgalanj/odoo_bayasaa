# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Scrolling news',
    'category': 'Extra tools',
    'sequence': 140,
    'website': 'https://www.linkedin.com/in/bayarbayasgalan-jagdal/',
    'author': 'Bayarbayasgalan MGL',
    'summary': 'News',
    'version': '1.0',
    'description': """
Scrolling Annoucement and link
============
        """,
    'depends': ['web','mail'],
    'data': [
        'security/bb_website_news.xml',
        'views/bb_website_news_view.xml',
        'security/ir.model.access.csv',
        'views/bb_website_news_templates.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml'
    ],
    "images": ["static/description/images/module_main_background.gif","static/description/images/bb_ss1.png","static/description/images/bb_ss2.png","static/description/images/bb_ss3.png"],
    'installable': True,
    'application': True,
    'icon': '/bb_website_news/static/description/icon.png',
}
