
{
    'name': "Open Academy",
    'sequence': 3,
    'summary': """Manage trainings""",

    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,

    'author': "KARIZMA CONSEIL",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board'],

    'qweb': ['static/src/xml/test.xml'],

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/openacademy.xml',
        'views/partner.xml',
        'views/session_board.xml',
        'reports.xml',
        'assets.xml',
        'views/openacademy_portal_templates.xml',
        'views/analysis.xml',
    ],
    
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
