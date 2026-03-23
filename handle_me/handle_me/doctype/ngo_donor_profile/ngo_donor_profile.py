# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class NGODonorProfile(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		aadhaar_number: DF.Data | None
		address_line_1: DF.Data | None
		address_line_2: DF.Data | None
		city: DF.Data | None
		consent_timestamp: DF.Datetime | None
		country: DF.Link | None
		date_of_birth: DF.Date | None
		donor: DF.Link
		donor_type: DF.Literal["Individual", "Company", "Trust", "Foundation", "CSR Entity", "Other"]
		email: DF.Data
		full_name: DF.Data
		gstin: DF.Data | None
		kyc_status: DF.Literal["Pending", "Verified", "Rejected"]
		last_login: DF.Datetime | None
		mobile: DF.Phone | None
		notes: DF.SmallText | None
		organization_name: DF.Data | None
		pan_number: DF.Data | None
		pincode: DF.Data | None
		portal_enabled: DF.Check
		preferred_communication: DF.Literal["Email", "SMS", "WhatsApp", "Phone"]
		receive_email_updates: DF.Check
		receive_sms_updates: DF.Check
		state: DF.Data | None
		user: DF.Link
	# end: auto-generated types

	pass
