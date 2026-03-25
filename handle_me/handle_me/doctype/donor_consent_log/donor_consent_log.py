# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class DonorConsentLog(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		consent_status: DF.Literal["Granted", "Withdrawn", "Pending"]
		consent_text_version: DF.Data | None
		consent_time: DF.Datetime
		consent_type: DF.Literal["Email Updates", "SMS Updates", "WhatsApp Updates", "Privacy Policy Acceptance", "Terms Acceptance", "PAN Declaration", "Tax Certificate Consent", "Data Correction Request"]
		donor: DF.Link
		donor_profile: DF.Link
		ip_address: DF.Data | None
		naming_series: DF.Literal["CONS-.YYYY.-"]
		notes: DF.SmallText | None
		recorded_by: DF.Link | None
		related_doctype: DF.Link | None
		related_document: DF.DynamicLink | None
		source: DF.Literal["Website", "Donor Portal", "Admin Entry", "Import", "API"]
		source_url: DF.Data | None
		user_agent: DF.SmallText | None
	# end: auto-generated types

	pass
