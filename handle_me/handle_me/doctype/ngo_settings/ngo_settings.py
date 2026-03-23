# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class NGOSettings(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		address_line_1: DF.Data
		address_line_2: DF.Data | None
		authorized_signatory_designation: DF.Data | None
		authorized_signatory_name: DF.Data
		city: DF.Data
		company: DF.Link
		corpus_fund_account: DF.Link | None
		country: DF.Link
		default_currency: DF.Link
		domestic_donation_account: DF.Link | None
		donation_cost_center: DF.Link | None
		email: DF.Data
		fcra_bank_account_no: DF.Data | None
		fcra_bank_name: DF.Data | None
		fcra_enabled: DF.Check
		fcra_registration_no: DF.Data | None
		fcra_valid_upto: DF.Date | None
		foreign_donation_account: DF.Link | None
		logo: DF.AttachImage | None
		ngo_name: DF.Data
		ngo_pan: DF.Data
		organization_type: DF.Literal["Trust", "Society", "Section 8 Company"]
		payment_gateway_enabled: DF.Check
		phone: DF.Phone | None
		pincode: DF.Data
		privacy_policy_url: DF.Data | None
		receipt_footer: DF.SmallText | None
		receipt_prefix: DF.Data
		registration_12ab: DF.Data | None
		registration_12ab_from: DF.Date | None
		registration_12ab_upto: DF.Date | None
		registration_80g: DF.Data | None
		registration_80g_from: DF.Date | None
		registration_80g_upto: DF.Date | None
		registration_date: DF.Date | None
		registration_number: DF.Data | None
		short_name: DF.Data | None
		state: DF.Data
		terms_url: DF.Data | None
		website: DF.Data | None
	# end: auto-generated types

	pass
