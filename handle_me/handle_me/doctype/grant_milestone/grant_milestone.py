# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class GrantMilestone(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amount_expected: DF.Currency
		attachment: DF.Attach | None
		dependency_note: DF.SmallText | None
		due_date: DF.Date | None
		milestone_title: DF.Data | None
		milestone_type: DF.Literal["Proposal", "Document Submission", "Approval", "Disbursement", "Utilization Report", "Impact Report", "Closure"]
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		remarks: DF.SmallText | None
		status: DF.Literal["Pending", "In Progress", "Completed", "Delayed", "Cancelled"]
		user: DF.Link | None
	# end: auto-generated types

	pass
