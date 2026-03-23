# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class DonationAllocation(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		allocation_type: DF.Literal["Program", "Fund", "Branch", "General"]
		amount: DF.Currency
		branch: DF.Link | None
		fund: DF.Link | None
		is_primary_allocation: DF.Check
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		percentage: DF.Percent
		program: DF.Link | None
		remarks: DF.SmallText | None
		restriction_note: DF.SmallText | None
	# end: auto-generated types

	pass
