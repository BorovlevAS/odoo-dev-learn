# -*- coding: utf-8 -*-
{
    'name': "BIKO: open academy 15.1.0.7",

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
    'version': '1.0.7',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board'],

    # always loaded
    'data': [
        'security/biko_oa_groups.xml',
        'security/biko_oa_course_security.xml',
        'security/ir.model.access.csv',
        'views/biko_oa_course_views.xml',
        'views/biko_oa_sessions_views.xml',
        'views/res_partner_views.xml',
        'wizards/biko_oa_wizard_views.xml',
        'views/biko_oa_sessions_dashboard.xml',
        'views/biko_oa_menus.xml',
        'reports/biko_oa_templates.xml',
        'reports/biko_oa_reports.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/biko_oa_course_demo.xml',
        'demo/biko_oa_sessions_demo.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
