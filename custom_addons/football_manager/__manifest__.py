{
    'name': 'Football Manager',
    'version': '1.0',
    'category': 'Extra Tools',
    'summary': 'A simple Football Manager game for Odoo',
    'description': 'A simple Football Manager game for Odoo',
    'author': 'Your Name',
    'website': 'https://www.example.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/team_view.xml',
        'views/player_view.xml',
        'views/match_views.xml',
        'views/menu.xml',
        'views/championship_view.xml',

    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
