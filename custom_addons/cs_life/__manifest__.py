{
    'name': 'CS Life',
    'version': '1.0',
    'category': 'Extra Tools',
    'summary': 'Cs',
    'description': 'CS',
    'author': 'Espadas',
    'website': '',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/cs_event_view.xml',
        'views/cs_match_view.xml',
        'views/cs_team_view.xml',
        'views/cs_menus.xml',
        'views/cs_actions.xml',
        'data/ir_cron_fetch_cs_data.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
