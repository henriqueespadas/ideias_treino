{
    'name': 'CS Guesses',
    'version': '1.0',
    'category': 'Extra Tools',
    'summary': 'Cs',
    'description': 'CS',
    'author': 'Espadas',
    'website': '',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/csg_match_view.xml',
        'views/csg_opponent_view.xml',
        'views/csg_actions.xml',
        'views/csg_menus.xml',
        'data/ir_cron_fetch_cs_data.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
