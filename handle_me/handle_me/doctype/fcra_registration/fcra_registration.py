# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FCRARegistration(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		bank_branch: DF.Data | None
		fcra_registration_no: DF.Data
		last_annual_return_date: DF.Date | None
		last_annual_return_fy: DF.Link | None
		mha_login_id: DF.Data | None
		next_annual_return_due: DF.Date | None
		ngo_legal_name: DF.Data
		nil_return_required: DF.Check
		pan: DF.Data
		registration_certificate: DF.Attach | None
		registration_date: DF.Date | None
		registration_name: DF.Data
		registration_type: DF.Literal["Registration", "Prior Permission"]
		remarks: DF.SmallText | None
		renewal_reminder_days: DF.Int
		responsible_user: DF.Link | None
		sbi_fcra_account_no: DF.Data | None
		sbi_fcra_bank_name: DF.Data | None
		status: DF.Literal["Draft", "Active", "Expired", "Suspended", "Renewal In Process"]
		valid_upto: DF.Date | None
	# end: auto-generated types

	pass
