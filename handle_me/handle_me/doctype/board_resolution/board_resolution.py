# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class BoardResolution(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		chairperson: DF.Data | None
		effective_date: DF.Date | None
		full_text: DF.TextEditor
		meeting_type: DF.Literal["Board Meeting", "General Meeting", "Executive Committee Meeting", "Trustee Meeting"]
		minutes_attachment: DF.Attach | None
		naming_series: DF.Literal["BR-.YYYY.-"]
		notes: DF.SmallText | None
		passed_by: DF.Data | None
		requires_roc_filing: DF.Check
		resolution_attachment: DF.Attach | None
		resolution_category: DF.Literal["Bank Signatory", "Grant Approval", "Annual Accounts Approval", "Statutory Filing Approval", "Appointment", "Property/Asset", "Policy Approval", "Borrowing", "Other"]
		resolution_date: DF.Data
		resolution_number: DF.Data | None
		resolution_title: DF.Data
		responsible_user: DF.Link | None
		roc_filing_due_date: DF.Date | None
		roc_form_reference: DF.Data | None
		status: DF.Literal["Draft", "Approved", "Filed", "Closed", "Cancelled"]
		summary: DF.SmallText | None
	# end: auto-generated types

	pass
