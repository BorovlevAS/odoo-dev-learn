# -*- coding: utf-8 -*-
{
    'name': "BIKO: open academy 15.1.0.6",

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
    'category': 'DEMO',
    'version': '1.0.6',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/courses_views.xml',
        'views/sessions_views.xml',
        'views/res_partner_views.xml',
        'wizards/wizard_views.xml',
        'views/menus.xml',
        'reports/reports.xml',
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
