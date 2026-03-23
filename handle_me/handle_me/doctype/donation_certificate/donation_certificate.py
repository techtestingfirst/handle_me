# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class DonationCertificate(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		certificate_number: DF.Data | None
		certificate_type: DF.Literal["10BE", "Annual Statement", "Receipt Copy", "Donation Summary"]
		donation_receipt: DF.Link | None
		donor_download_count: DF.Int
		donor_download_enabled: DF.Check
		donor_name: DF.Data
		donor_pan: DF.Data | None
		donor_profile: DF.Link
		eligible_amount: DF.Currency
		erpnext_donation: DF.Link | None
		erpnext_donor: DF.Link
		file: DF.Attach
		financial_year: DF.Link
		form_10bd_batch_ref: DF.Data | None
		issue_date: DF.Date
		issued_by: DF.Link | None
		last_downloaded_on: DF.Datetime | None
		naming_series: DF.Literal["CERT-.YYYY.-"]
		remarks: DF.SmallText | None
		status: DF.Literal["Draft", "Issued", "Withdrawn", "Reissued"]
		total_donation_amount: DF.Currency
	# end: auto-generated types

	pass
