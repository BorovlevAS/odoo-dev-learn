# -*- coding: utf-8 -*-
{
    'name': "BIKO: Academy",

    'summary': """
        BIKO: Academy
        """,

    'description': """
        BIKO: academy website
    """,

    'author': "BIKO",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'DEMO',
    'version': '1.0.1',

    # any module necessary for this one to work correctly
    'depends': ['website_sale', 'mail'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'templates/templates.xml',
        'views/views.xml',
        'data/data.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
