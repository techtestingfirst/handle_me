# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class DonationIntent(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from handle_me.handle_me.doctype.donation_allocation.donation_allocation import DonationAllocation

		allocations: DF.Table[DonationAllocation]
		amount: DF.Currency
		currency: DF.Link
		donation_type: DF.Literal["One Time", "Recurring", "Corpus", "In-Kind"]
		donor_name: DF.Data
		donor_profile: DF.Link
		email: DF.Data
		erpnext_donation: DF.Link | None
		erpnext_donor: DF.Link
		fund: DF.Link | None
		gateway_order_id: DF.Data | None
		gateway_payment_id: DF.Data | None
		intent_date: DF.Date
		ip_address: DF.Data | None
		is_anonymous: DF.Check
		message: DF.SmallText | None
		mobile: DF.Phone | None
		naming_series: DF.Literal["DI-.YYYY.-"]
		pan_number: DF.Data | None
		payment_gateway: DF.Data | None
		payment_request: DF.Link | None
		program: DF.Link | None
		receipt_generated: DF.Check
		remarks: DF.SmallText | None
		source: DF.Literal["Website", "Donor Portal", "Admin Entry", "Campaign Link"]
		status: DF.Literal["Draft", "Pending Payment", "Payment Requested", "Paid", "Failed", "Cancelled", "Expired"]
		user_agent: DF.SmallText | None
	# end: auto-generated types

	pass
