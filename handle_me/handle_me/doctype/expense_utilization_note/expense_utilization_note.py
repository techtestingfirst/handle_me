# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ExpenseUtilizationNote(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		amount: DF.Currency
		approved_by: DF.Link | None
		branch: DF.Link | None
		currency: DF.Link
		donor: DF.Link | None
		fund: DF.Link | None
		grant_award: DF.Link | None
		naming_series: DF.Literal["EUN-.YYYY.-"]
		notes: DF.SmallText | None
		posting_date: DF.Date
		program: DF.Link | None
		reference_name: DF.Data | None
		reference_type: DF.Literal["Expense Claim", "Purchase Invoice", "Journal Entry", "Payment Entry", "Manual"]
		supporting_document: DF.Attach | None
		utilization_status: DF.Literal["Draft", "Approved", "Partially Supported", "Rejected"]
		utilization_summary: DF.SmallText | None
		utilization_type: DF.Literal["Program Expense", "Administrative Expense", "Capital Expense", "Staff Cost", "Travel", "Material Distribution", "Other"]
	# end: auto-generated types

	pass
