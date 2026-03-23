# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class NGOFund(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		allow_public_donations: DF.Check
		company: DF.Link
		cost_center: DF.Link | None
		default_account: DF.Link | None
		end_date: DF.Date | None
		fund_code: DF.Data | None
		fund_description: DF.TextEditor | None
		fund_name: DF.Data
		fund_type: DF.Literal["General", "Restricted", "Corpus", "CSR", "Grant", "FCRA"]
		is_corpus_fund: DF.Check
		is_foreign_fund: DF.Check
		requires_donor_restriction: DF.Check
		start_date: DF.Date | None
		status: DF.Literal["Active", "Inactive", "Closed"]
		usage_notes: DF.SmallText | None
	# end: auto-generated types

	pass
