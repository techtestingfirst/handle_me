# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class NGOProgram(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		accept_donations: DF.Check
		amount_raised: DF.Currency
		banner_image: DF.AttachImage | None
		beneficiary_target: DF.Int
		branch: DF.Link | None
		description: DF.TextEditor | None
		end_date: DF.Date | None
		fund: DF.Link | None
		goal_amount: DF.Currency
		impact_summary: DF.SmallText | None
		is_restricted_program: DF.Check
		notes: DF.SmallText | None
		program_code: DF.Data | None
		program_manager: DF.Link | None
		program_name: DF.Data
		program_type: DF.Literal["Education", "Healthcare", "Livelihood", "Relief", "Environment", "Women Empowerment", "Child Welfare", "Skill Development", "Other"]
		public_title: DF.Data | None
		requires_utilization_report: DF.Check
		route: DF.Data | None
		short_description: DF.SmallText | None
		show_on_website: DF.Check
		start_date: DF.Date | None
		status: DF.Literal["Draft", "Active", "On Hold", "Completed", "Closed"]
		suggested_amount: DF.Currency
	# end: auto-generated types

	pass
