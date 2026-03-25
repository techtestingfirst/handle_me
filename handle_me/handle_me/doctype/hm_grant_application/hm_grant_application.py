# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class HMGrantApplication(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from handle_me.handle_me.doctype.grant_milestone.grant_milestone import GrantMilestone

		application_date: DF.Date
		application_type: DF.Literal["CSR", "Foundation", "Government", "International", "Emergency", "Recurring"]
		branch: DF.Link
		budget_file: DF.Attach | None
		contact_person: DF.Data | None
		currency: DF.Link
		end_date: DF.Date | None
		expected_decision_date: DF.Date | None
		grantor: DF.Link
		milestones: DF.Table[GrantMilestone]
		naming_series: DF.Literal["GA-.YYYY.-"]
		program: DF.Link
		proposal_file: DF.Attach | None
		proposal_summary: DF.TextEditor | None
		remarks: DF.SmallText | None
		requested_amount: DF.Currency
		start_date: DF.Date | None
		status: DF.Literal["Draft", "Submitted", "Under Review", "Clarification Requested", "Approved", "Rejected", "Withdrawn"]
		submitted_by: DF.Link | None
		title: DF.Data
	# end: auto-generated types

	pass
