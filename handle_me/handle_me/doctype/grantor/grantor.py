# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Grantor(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		address_line_1: DF.Data | None
		address_line_2: DF.Data | None
		cin: DF.Data | None
		city: DF.Data | None
		contact_person: DF.Data | None
		country: DF.Link | None
		csr_1_available: DF.Check
		csr_1_required: DF.Check
		email: DF.Data | None
		grantor_name: DF.Data
		grantor_type: DF.Literal["CSR Company", "Foundation", "Government", "Trust", "International Agency", "High Net Worth Individual", "Other"]
		mobile: DF.Phone | None
		notes: DF.SmallText | None
		pan: DF.Data | None
		phone: DF.Phone | None
		pincode: DF.Data | None
		preferred_program_area: DF.Data | None
		state: DF.Data | None
		status: DF.Literal["Prospect", "Active", "Inactive", "Blacklisted"]
		website: DF.Data | None
	# end: auto-generated types

	pass
