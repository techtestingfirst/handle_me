# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class PortalAccessLog(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		access_time: DF.Datetime
		donor_profile: DF.Link | None
		event_type: DF.Literal["Login", "Logout", "Dashboard View", "Donation Initiated", "Donation Completed", "Receipt Download", "Certificate Download", "Profile Update", "Password Reset"]
		failure_reason: DF.SmallText | None
		ip_address: DF.Data | None
		naming_series: DF.Literal["PAL-.YYYY.-"]
		notes: DF.SmallText | None
		related_doctype: DF.Link | None
		related_document: DF.DynamicLink | None
		session_id: DF.Data | None
		status: DF.Literal["Success", "Failed", "Blocked"]
		user: DF.Link
		user_agent: DF.SmallText | None
	# end: auto-generated types

	pass
