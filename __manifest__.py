# -*- coding: utf-8 -*-
{
    'name': 'Ventas Dashboard / Vista de tarjetas',
    'version': '1.0',
    'summary': """ Módulo que permite ver indicadores como tarjetas de ventas en la vista lista """,
    'author': 'Breithner Aquituari',
    'website': '',
    'category': 'Sale',
    'depends': ['sale_management', 'sale', 'base' ],
    "data": [
        "views/res_users_views.xml",
        "views/sale_order_views.xml"
    ],

    'assets': {
        'web.assets_backend': [
            'owl_sale_dashboard/static/**/*',
            # 'owl_sale_dashboard/static/src/views/sale_listview.js',
            # 'owl_sale_dashboard/static/src/views/sale_dashboard.xml',
            # 'owl_sale_dashboard/static/src/views/sale_listview.xml',
        ]
    },
    
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
