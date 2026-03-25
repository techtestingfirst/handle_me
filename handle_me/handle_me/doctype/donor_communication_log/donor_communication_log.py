# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class DonorCommunicationLog(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		attachment: DF.Attach | None
		communication_date: DF.Datetime
		communication_type: DF.Literal["Email", "SMS", "WhatsApp", "Phone", "Portal Notification", "Manual Note"]
		direction: DF.Literal["Outgoing", "Incoming"]
		donor: DF.Link | None
		donor_profile: DF.Link
		email_address: DF.Data | None
		error_log: DF.SmallText | None
		message_summary: DF.SmallText
		mobile_number: DF.Phone | None
		naming_series: DF.Literal["DCL-.YYYY.-"]
		notes: DF.SmallText | None
		related_doctype: DF.Link | None
		related_document: DF.DynamicLink | None
		sent_by: DF.Link | None
		status: DF.Literal["Draft", "Queued", "Sent", "Delivered", "Failed", "Received", "Read"]
		subject: DF.Data | None
		template_used: DF.Data | None
	# end: auto-generated types

	pass
