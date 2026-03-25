# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class VolunteerAssignment(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		actual_hours: DF.Float
		assignment_date: DF.Date
		assignment_type: DF.Literal["Event", "Field Work", "Teaching", "Fundraising", "Counselling", "Administration", "Awareness Campaign", "Other"]
		branch: DF.Link | None
		end_date: DF.Date | None
		estimated_hours: DF.Float
		feedback_received: DF.Check
		naming_series: DF.Literal["VA-.YYYY.-"]
		orientation_completed: DF.Check
		performance_notes: DF.SmallText | None
		program: DF.Link | None
		remarks: DF.SmallText | None
		role_title: DF.Data
		start_date: DF.Date
		status: DF.Literal["Planned", "Active", "Completed", "Cancelled", "No Show"]
		supervisor: DF.Link | None
		volunteer: DF.Link
	# end: auto-generated types

	pass
