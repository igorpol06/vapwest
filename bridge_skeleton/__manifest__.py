# -*- coding: utf-8 -*-
##########################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
##########################################################################

{
    'name': 'Odoo: Bridge Skeleton',
    'version': '4.0.0',
    'category': 'Bridge Module',
    'author': 'Webkul Software Pvt. Ltd.',
    'website': 'https://store.webkul.com/Magento-OpenERP-Bridge.html',
    'summary': 'Core of Webkul Bridge Modules',
    "license":  "Other proprietary",
    'description': """
        This is core for all basic operations features provided in Webkul's Bridge Modules.
    """,
    'images': [],
    'depends': [
        'delivery',
        'account_payment',
    ],
    'data': [
        'security/connector_security.xml',
        'security/ir.model.access.csv',
        'wizard/message_wizard_view.xml',
        'wizard/api_details_wizard_view.xml',
        'wizard/synchronization_wizard_view.xml',
        'wizard/status_synchronization_wizard_view.xml',
        'data/connector_sequence.xml',
        'data/connector_server_actions.xml',
        'data/order_status_server_actions.xml',
        'views/core/sale_views.xml',
        'views/core/product_template_views.xml',
        'views/core/product_views.xml',
        'views/core/res_partner_view.xml',
        'views/core/stock_picking_views.xml',
        'views/core/account_move_view.xml',
        'views/base/connector_instance_view.xml',
        'views/mapping/connector_attribute_mapping_view.xml',
        'views/mapping/connector_options_mapping_view.xml',
        'views/mapping/connector_category_mapping_view.xml',
        'views/mapping/connector_template_mapping_view.xml',
        'views/mapping/connector_product_mapping_view.xml',
        'views/mapping/connector_partner_mapping_view.xml',
        'views/mapping/connector_order_mapping_view.xml',
        'views/base/connector_sync_history_view.xml',
        'views/dashboard/connector_dashboard_view.xml',
        'views/dashboard/dashboard_extend_view.xml',
        'views/base/connector_snippet.xml',
        'views/base/connector_menus.xml',
    ],
    'qweb': ['static/src/xml/skeleton_kanban.xml', ],
    'assets': {
        'web.assets_backend': [
                '/bridge_skeleton/static/src/scss/connector_kanban.scss',
                '/bridge_skeleton/static/src/scss/skeleton_kanban.scss',
                '/bridge_skeleton/static/src/js/skeleton_kanban_widget.js',
                '/bridge_skeleton/static/src/js/skeleton_kanban_view.js',
                '/bridge_skeleton/static/src/js/skeleton_kanban_controller.js',
                '/bridge_skeleton/static/src/js/skeleton_kanban_renderer.js',
                '/bridge_skeleton/static/src/js/skeleton_kanban_model.js',
                '/bridge_skeleton/static/src/js/skeleton_kanban_record.js',
                '/bridge_skeleton/static/src/js/skeleton_kanban_mobile.js',
        ],
        'web.assets_qweb': [
                '/bridge_skeleton/static/src/xml/skeleton_kanban.xml',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
    # 'pre_init_hook': 'pre_init_check',
}
