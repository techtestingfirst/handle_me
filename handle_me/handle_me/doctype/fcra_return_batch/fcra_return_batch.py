# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FCRAReturnBatch(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		acknowledgement_no: DF.Data | None
		administrative_expenses: DF.Currency
		audit_attachment: DF.Attach | None
		bank_statement_attachment: DF.Attach | None
		due_date: DF.Date | None
		error_log: DF.SmallText | None
		fcra_registration: DF.Link
		filing_date: DF.Date | None
		filing_status: DF.Literal["Draft", "Prepared", "Under Audit", "Ready to File", "Filed", "Revised", "Nil Return Filed"]
		financial_year: DF.Link
		naming_series: DF.Literal["FC4-.FY.-"]
		nil_return: DF.Check
		notes: DF.SmallText | None
		prepared_by: DF.Link | None
		return_attachment: DF.Attach | None
		reviewed_by: DF.Link | None
		total_foreign_receipts: DF.Currency
		total_utilization: DF.Currency
	# end: auto-generated types

	pass
