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

    'images': [
        'static/description/kea_description.png',
        'static/description/kea_screenshot.jpg',
    ],
    'images_preview_theme': {
        'website.s_cover_default_image': '/theme_biko_web/static/src/img/s_cover.jpg',
        'website.s_picture_default_image': '/theme_biko_web/static/src/img/s_picture.jpg',
    },

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