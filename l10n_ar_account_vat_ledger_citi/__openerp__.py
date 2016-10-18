# -*- coding: utf-8 -*-
{
    "name": "Argentinian CITI Reports",
    'version': '9.0.1.0.0',
    'category': 'Localization/Argentina',
    'sequence': 14,
    'author': 'ADHOC SA,Moldeo Interactive',
    'license': 'AGPL-3',
    'summary': '',
    "depends": [
        "l10n_ar_account_vat_ledger",
    ],
    'external_dependencies': {
    },
    "data": [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/account_vat_report_view.xml',
        'views/afip_document_class_view.xml',
        'data/afip.document_class.csv',
    ],
    'demo': [
    ],
    'test': [
    ],
    'images': [
    ],
    'installable': False,
    'auto_install': True,
    'application': False,
}
