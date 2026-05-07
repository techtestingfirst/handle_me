# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt


import frappe
from frappe import _
from frappe.model.document import Document


class MembershipType(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amount: DF.Float
		linked_item: DF.Link | None
		membership_type: DF.Data
		razorpay_plan_id: DF.Data | None
	# end: auto-generated types

	def validate(self):
		if self.linked_item:
			is_stock_item = frappe.db.get_value("Item", self.linked_item, "is_stock_item")
			if is_stock_item:
				frappe.throw(_("The Linked Item should be a service item"))

def get_membership_type(razorpay_id):
	return frappe.db.exists("Membership Type", {"razorpay_plan_id": razorpay_id})
