# -*- coding: utf-8 -*-
{
    'name': "Purchase Request",
    'summary': "Purchase Request Workflow",
    'description': "Purchase Request Workflow",
    'author': "Zadsolutions",
    'website': "http://www.zadsolutions.com",
    'category': 'Purchase',
    'version': '13.0.0.0.1',
    'depends': ['purchase', 'base', ],
    'data': [
        "security/ir.model.access.csv",
        'wizards/wizard_view.xml',
        'views/email_temp.xml',
        'report/report_view.xml',
        'views/purchase_request_view.xml',
    ],
}
