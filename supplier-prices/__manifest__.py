{
    'name': "A: supplier prices",
    'version': '15.0.0',
    'depends': ['base'],
    'author': "Author Name",
    'category': 'CRM',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        'demo/demo.xml',
    ],
}