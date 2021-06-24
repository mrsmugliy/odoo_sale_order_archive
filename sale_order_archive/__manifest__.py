# -*- coding: utf-8 -*-
{
    'name': "Sale Order Archive",
    'description': """
        Sale Order Archive module
    """,
    'version': '0.1',
    'depends': ['base', 'base_setup', 'sale_management', 'mail'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/archiving_orders_cron.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'sequence': 1,
    'installable': True,
    'application': True,
    'auto_install': False,
}
