# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt


from frappe.contacts.address_and_contact import load_address_and_contact
from frappe.model.document import Document


class Volunteer(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from handle_me.handle_me.doctype.volunteer_skill.volunteer_skill import VolunteerSkill

		availability: DF.Literal["", "Weekly", "Weekdays", "Weekends"]
		availability_timeslot: DF.Literal["", "Morning", "Afternoon", "Evening", "Anytime"]
		email: DF.Data
		image: DF.AttachImage | None
		note: DF.LongText | None
		volunteer_name: DF.Data
		volunteer_skills: DF.Table[VolunteerSkill]
		volunteer_type: DF.Link
	# end: auto-generated types

	def onload(self):
		"""Load address and contacts in `__onload`"""
		load_address_and_contact(self)
