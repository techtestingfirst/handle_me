# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class NGOBranch(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		address_line_1: DF.Data
		address_line_2: DF.Data | None
		branch_code: DF.Data | None
		branch_head: DF.Link | None
		branch_name: DF.Data | None
		branch_type: DF.Literal["Head Office", "Regional Office", "Project Office", "Field Office", "Collection Center"]
		city: DF.Data
		cost_center: DF.Link | None
		country: DF.Link
		district: DF.Data | None
		email: DF.Data | None
		is_donation_collection_point: DF.Check
		is_program_delivery_branch: DF.Check
		linked_company: DF.Link | None
		notes: DF.SmallText | None
		phone: DF.Phone | None
		pincode: DF.Data
		state: DF.Data
		status: DF.Literal["Active", "Inactive", "Closed"]
	# end: auto-generated types

	pass
