# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class NGOComplianceCalendar(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		branch: DF.Link | None
		completion_attachment: DF.Attach | None
		completion_date: DF.Date | None
		compliance_title: DF.Data
		compliance_type: DF.Literal["Form 10BD", "Form 10BE", "12AB Renewal", "80G Renewal", "FCRA Return", "Audit Filing", "ITR-7 Filing", "Board Meeting", "CSR Reporting", "Other"]
		description: DF.SmallText | None
		due_date: DF.Date
		naming_series: DF.Literal["CC-.YYYY.-"]
		priority: DF.Literal["Low", "Medium", "High", "Critical"]
		related_doctype: DF.Link | None
		related_document: DF.DynamicLink | None
		related_financial_year: DF.Link | None
		remarks: DF.SmallText | None
		reminder_date: DF.Date | None
		responsible_user: DF.Link | None
		status: DF.Literal["Upcoming", "In Progress", "Completed", "Overdue", "Cancelled"]
	# end: auto-generated types

	pass
