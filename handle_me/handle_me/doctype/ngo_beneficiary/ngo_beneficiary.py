# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class NGOBeneficiary(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		aadhaar_number: DF.Data | None
		address_line_1: DF.Data | None
		address_line_2: DF.Data | None
		beneficiary_id: DF.Data | None
		beneficiary_type: DF.Literal["Individual", "Family", "Group", "Institution"]
		branch: DF.Link | None
		category: DF.Literal["Child", "Woman", "Senior Citizen", "Farmer", "Student", "Patient", "Family", "Differently Abled", "Other"]
		city: DF.Data | None
		country: DF.Link | None
		date_of_birth: DF.Date | None
		district: DF.Data | None
		email: DF.Data | None
		full_name: DF.Data
		gender: DF.Literal["Male", "Female", "Other", "Prefer Not to Say"]
		guardian_name: DF.Data | None
		id_proof: DF.Attach | None
		mobile: DF.Phone | None
		needs_assessment: DF.TextEditor | None
		notes: DF.SmallText | None
		photo: DF.AttachImage | None
		pincode: DF.Data | None
		program: DF.Link | None
		registration_date: DF.Date | None
		state: DF.Data | None
		status: DF.Literal["Active", "Inactive", "Exited", "On Hold"]
		verification_status: DF.Literal["Pending", "Verified", "Rejected"]
	# end: auto-generated types

	pass
