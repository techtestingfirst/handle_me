# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class TaxExemptionRegistration(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		approval_date: DF.Date | None
		issuing_authority: DF.Data | None
		last_renewal_date: DF.Date | None
		next_action_date: DF.Date | None
		notes: DF.SmallText | None
		order_copy: DF.Attach | None
		order_reference: DF.Data | None
		organization_name: DF.Data
		pan: DF.Data
		registration_name: DF.Data
		registration_number: DF.Data
		registration_type: DF.Literal["12AB", "80G"]
		renewal_reminder_days: DF.Int
		responsible_user: DF.Link | None
		status: DF.Literal["Draft", "Active", "Expired", "Suspended", "Renewal In Process"]
		valid_from: DF.Date | None
		valid_upto: DF.Date | None
	# end: auto-generated types

	pass
