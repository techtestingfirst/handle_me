# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class StatutoryDocument(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		attachment: DF.Attach | None
		description: DF.SmallText | None
		document_name: DF.Data
		document_number: DF.Data | None
		document_type: DF.Literal["PAN", "Trust Deed", "Society Registration", "Section 8 Certificate", "12AB Order", "80G Order", "FCRA Certificate", "Audit Report", "ITR Acknowledgement", "10BD Acknowledgement", "10BE Sample", "CSR-1", "Board Resolution", "Bank Proof", "Other"]
		is_mandatory: DF.Check
		issue_date: DF.Date | None
		issuing_authority: DF.Data | None
		notes: DF.SmallText | None
		owner_user: DF.Link | None
		related_doctype: DF.Link | None
		related_document_name: DF.DynamicLink | None
		reminder_days_before_expiry: DF.Int
		status: DF.Literal["Draft", "Active", "Expired", "Archived", "Superseded"]
		valid_from: DF.Date | None
		valid_upto: DF.Date | None
	# end: auto-generated types

	pass
