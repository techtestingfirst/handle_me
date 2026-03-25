# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Form10BDDonorRow(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		aadhaar_number: DF.Data | None
		address_line_1: DF.Data | None
		city: DF.Data | None
		country: DF.Link | None
		donation_amount: DF.Currency
		donation_date: DF.Date | None
		donation_type: DF.Literal["Corpus", "Specific Grant", "Others"]
		donor: DF.Link | None
		donor_name: DF.Data | None
		donor_profile: DF.Link | None
		donor_type: DF.Literal["Individual", "Organization", "Other"]
		eligible_amount: DF.Currency
		pan_number: DF.Data | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		pincode: DF.Data | None
		receipt_reference: DF.Link | None
		remarks: DF.SmallText | None
		section_code: DF.Literal["80G"]
		state: DF.Data | None
		tax_id_type: DF.Literal["PAN", "Aadhaar", "Passport", "Other ID"]
	# end: auto-generated types

	pass
