# -*- coding: utf-8 -*-
{
    'name': "BIKO: Partner Card - 15.0.3",

    'summary': 'BIKO: partner card for ODOO',

    'description': """
        Partner's card will be usefull for saving information about partners.
        It's date of first contact, name of CEO, common information, description, etc.
    """,

    'author': "BIKO solutions",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'PRM',
    'version': '15.0.3',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/biko_partners_card_views.xml',
        'views/biko_menu_items.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
