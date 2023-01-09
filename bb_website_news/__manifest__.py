# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Scrolling news',
    'category': 'Extra tools',
    'sequence': 140,
    'website': 'https://www.linkedin.com/in/bayarbayasgalan-jagdal/',
    'author': 'Bayarbayasgalan MGL',
    'summary': 'Scrolling Annoucement and link, Attention announcements',
    'version': '15.0.0.1',
    'description': """
Scrolling Annoucement and link
============
        """,
    'depends': ['web','mail'],
    'data': [
        'security/bb_website_news.xml',
        'views/bb_website_news_view.xml',
        'security/ir.model.access.csv',
    ],
    # 'qweb': [
    #     'static/src/xml/*.xml'
    # ],
    "images": ["static/description/images/bb_ss1.png","static/description/images/bb_ss2.png","static/description/images/bb_ss3.png"],

    'assets': {
        'web.assets_qweb': [
            'bb_website_news/static/src/xml/bb_website_news.xml'
        ],
        'web.assets_backend': [
            'bb_website_news/static/src/css/website_news.css',
            'bb_website_news/static/lib/jquery.marquee.js',
            'bb_website_news/static/src/js/website_news.js',
        ],
        
    },
    'installable': True,
    'application': True,
    'icon': '/bb_website_news/static/description/icon.png',
    'license': 'LGPL-3',
}
