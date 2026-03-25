# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class HMVolunteer(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from handle_me.handle_me.doctype.volunteer_skill_row.volunteer_skill_row import VolunteerSkillRow

		address_line_1: DF.Data | None
		address_line_2: DF.Data | None
		availability: DF.Literal["Weekdays", "Weekends", "Evenings", "Full Time", "On Call"]
		background_check_status: DF.Literal["Not Required", "Pending", "Verified", "Rejected"]
		branch: DF.Link | None
		city: DF.Data | None
		country: DF.Link | None
		date_of_birth: DF.Date | None
		email: DF.Data | None
		emergency_contact_name: DF.Data | None
		emergency_contact_phone: DF.Phone | None
		full_name: DF.Data
		gender: DF.Literal["Male", "Female", "Other", "Prefer Not to Say"]
		id_proof: DF.Attach | None
		mobile: DF.Phone | None
		notes: DF.SmallText | None
		onboarding_date: DF.Date | None
		pincode: DF.Data | None
		preferred_program: DF.Link | None
		skills: DF.SmallText | None
		skills_data: DF.Table[VolunteerSkillRow]
		state: DF.Data | None
		status: DF.Literal["Applicant", "Active", "Inactive", "Suspended", "Exited"]
		volunteer_agreement_signed: DF.Check
		volunteer_id: DF.Data | None
	# end: auto-generated types

	pass
