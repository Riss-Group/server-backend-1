# Copyright 2025 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import Command


def _post_init_hook(env):
    """Give group to admin at first install"""
    env.ref("base.user_admin").write(
        {
            "groups_id": [
                Command.link(
                    env.ref("base_user_group_mgmt.security_management_manager").id
                )
            ]
        }
    )
