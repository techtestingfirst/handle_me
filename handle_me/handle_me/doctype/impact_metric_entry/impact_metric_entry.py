# Copyright (c) 2026, Praveen Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ImpactMetricEntry(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		beneficiary_count: DF.Int
		branch: DF.Link | None
		entry_date: DF.Date
		evidence_file: DF.Attach | None
		female_count: DF.Int
		male_count: DF.Int
		metric_category: DF.Literal["Output", "Outcome", "Activity", "Coverage", "Volunteer", "Fundraising"]
		metric_name: DF.Data
		metric_value: DF.Float
		naming_series: DF.Literal["IME-.YYYY.-"]
		narrative: DF.SmallText | None
		other_count: DF.Int
		period_type: DF.Literal["Daily", "Weekly", "Monthly", "Quarterly", "Yearly", "One Time"]
		program: DF.Link
		unit_of_measure: DF.Data
		verified_by: DF.Link | None
		volunteer_hours: DF.Float
	# end: auto-generated types

	pass
