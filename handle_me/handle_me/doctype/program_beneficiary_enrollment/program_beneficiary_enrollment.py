# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ProgramBeneficiaryEnrollment(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		approved_budget: DF.Currency
		beneficiary: DF.Link
		branch: DF.Link
		case_worker: DF.Link | None
		end_date: DF.Date | None
		enrollment_date: DF.Date
		enrollment_status: DF.Literal["Applied", "Active", "Completed", "Dropped", "Transferred", "On Hold"]
		exit_reason: DF.SmallText | None
		naming_series: DF.Literal["PBE-.YYYY.-"]
		notes: DF.SmallText | None
		outcome_target: DF.SmallText | None
		priority_level: DF.Literal["Low", "Medium", "High", "Critical"]
		program: DF.Link
		referral_source: DF.Data | None
		service_type: DF.Literal["Education Support", "Medical Support", "Food Aid", "Livelihood Support", "Counselling", "Training", "Scholarship", "Other"]
		start_date: DF.Date | None
	# end: auto-generated types

	pass
