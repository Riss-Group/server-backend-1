# Copyright 2025 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResUsers(models.Model):

    _inherit = "res.users"

    # Odoo 19 : les champs de groupes "reified" (in_group_/sel_groups_) et le
    # helper is_reified_group ont été retirés du cœur (l'UI des droits d'accès
    # est désormais basée sur les privilèges, qui écrivent directement
    # group_ids). Rendre group_ids readonly suffit donc à figer l'affectation
    # des groupes (plus besoin de filtrer des champs virtuels au write()).
    group_ids = fields.Many2many(
        readonly=True,
    )
