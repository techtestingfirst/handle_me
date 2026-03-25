# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FCRAAnnualReturnRow(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		balance_amount: DF.Currency
		bank_reference: DF.Data | None
		country: DF.Link | None
		currency: DF.Link | None
		donor_name: DF.Data | None
		donor_type: DF.Literal["Individual", "Organization", "Foundation", "Government", "Other"]
		foreign_amount: DF.Currency
		fund: DF.Link | None
		inr_amount: DF.Currency
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		program: DF.Link | None
		purpose: DF.Data | None
		receipt_date: DF.Date | None
		remarks: DF.SmallText | None
		utilized_amount: DF.Currency
	# end: auto-generated types

	pass
