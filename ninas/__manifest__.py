# -*- coding: utf-8 -*-
# @author TK
# Date: 4/06/18


{
    'name': 'Ninas Academy', 
    'summary': 'Ninas Academy',
    'description': """ Ninas Academy
                        The best academy in MCEE. 
                        You won't believe what you can see. 
                    """,
    'author': 'Tosin K',
    'website': 'http://tosinkomolafe.com',
    'version': '10.0.0.0.1',
    'application':True,
    'installable':True,
    'auto-install':False,
    'depends': ['base', 'hr', 'mail'],
    'external_dependencies': {
        'python':[],
        'bin':[]
    },
    'data':['views/course_view.xml',
            'views/section_view.xml',
            'views/student_view.xml',
            'views/employee_view.xml',
            'views/menuitem_view.xml',
            'wizard/ninas_student_wizard_view.xml'
            ],
    'css':[],
    'demo_xml':[],
    'test':[],
}