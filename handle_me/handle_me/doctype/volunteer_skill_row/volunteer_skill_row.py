# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class VolunteerSkillRow(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		certification_file: DF.Attach | None
		certified: DF.Check
		notes: DF.SmallText | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		preferred_use_area: DF.Data | None
		skill_category: DF.Literal["Teaching", "Fundraising", "Technology", "Design", "Medical", "Counselling", "Administration", "Field Work", "Other"]
		skill_level: DF.Literal["Beginner", "Intermediate", "Advanced", "Expert"]
		skill_name: DF.Data | None
		years_experience: DF.Float
	# end: auto-generated types

	pass
