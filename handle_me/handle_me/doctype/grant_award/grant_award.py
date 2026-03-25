# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class GrantAward(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		agreement_file: DF.Attach | None
		amended_from: DF.Link | None
		award_date: DF.Date
		award_title: DF.Data
		branch: DF.Link | None
		currency: DF.Link
		disbursement_type: DF.Literal["One Time", "Milestone Based", "Quarterly", "Monthly", "Reimbursement"]
		end_date: DF.Date | None
		first_disbursement_date: DF.Date | None
		fund: DF.Link | None
		grant_application: DF.Link | None
		grantor: DF.Link
		naming_series: DF.Literal["GW-.YYYY.-"]
		program: DF.Link | None
		project_owner: DF.Link | None
		remarks: DF.SmallText | None
		restriction_type: DF.Literal["Unrestricted", "Program Restricted", "Time Restricted", "Corpus", "CSR Restricted"]
		sanctioned_amount: DF.Currency
		start_date: DF.Date | None
		status: DF.Literal["Draft", "Active", "Completed", "Closed", "Cancelled"]
		utilization_frequency: DF.Literal["Monthly", "Quarterly", "Half Yearly", "Yearly", "On Demand"]
		utilization_report_required: DF.Check
	# end: auto-generated types

	pass
