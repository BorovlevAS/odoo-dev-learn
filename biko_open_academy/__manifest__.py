# -*- coding: utf-8 -*-
{
    'name': "BIKO: open academy 15.1.0.5",

    'summary': """
        BIKO: open academy
        """,

    'description': """
        BIKO: open academy
    """,

    'author': "BIKO",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0.5',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/biko_oa_cources_views.xml',
        'views/biko_oa_sessions_views.xml',
        'views/menus.xml',
        'views/templates.xml',
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
