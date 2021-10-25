# Copyright 2021 Akretion (https://www.akretion.com).
# @author Pierrick Brun <pierrick.brun@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models

def _int_to_hour_minute(minutes):
    return "{:02d}:{:02d}".format(*divmod(int(minutes),60))

class ResourceCalendarAttendance(models.Model):
    _inherit = 'resource.calendar.attendance'

    available_online = fields.Boolean("Available online", default=True)

    hour_from_string = fields.Char(compute="_compute_hours_string", store=False, readonly=True)
    hour_to_string = fields.Char(compute="_compute_hours_string", store=False, readonly=True)

    @api.depends("hour_from", "hour_to")
    def _compute_hours_string(self):
        converter = self.env["ir.qweb.field.float_time"]
        for record in self:
            record.hour_from_string = converter.value_to_html(record.hour_from, None)
            record.hour_to_string = converter.value_to_html(record.hour_to, None)
