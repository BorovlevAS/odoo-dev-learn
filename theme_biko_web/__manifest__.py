{
    'name': 'BIKO: tutorial theme',
    'description': 'BIKO: tutorial theme',
    'version': '1.0.1',
    'author': 'BIKO',
    'category': 'Theme/Creative',

    'depends': ['website'],
    'data': [
        'views/layout.xml',
        'views/pages.xml',
        'views/snippets.xml',
        'views/options.xml',
    ],

    'assets': {
        'web.assets_frontend':[
            'theme_biko_web/static/scss/style.scss',
        ],
        'web._assets_primary_variables': [
            'theme_biko_web/static/scss/primary_variables.scss',
        ],
        'web._assets_frontend_helpers': [
            'theme_biko_web/static/scss/bootstrap_overriden.scss',
        ],
        'website.assets_editor': [
            'theme_biko_web/static/js/tutorial_editor.js',
        ]
    }
}