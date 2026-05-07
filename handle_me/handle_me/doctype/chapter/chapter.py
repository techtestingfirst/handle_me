# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt


import frappe
from frappe.website.website_generator import WebsiteGenerator


class Chapter(WebsiteGenerator):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from handle_me.handle_me.doctype.chapter_member.chapter_member import ChapterMember

		address: DF.Text | None
		chapter_head: DF.Link
		introduction: DF.TextEditor
		meetup_embed_html: DF.Code | None
		members: DF.Table[ChapterMember]
		published: DF.Check
		region: DF.Data
		route: DF.Data | None
	# end: auto-generated types

	_website = frappe._dict(
		condition_field = "published",
	)

	def get_context(self, context):
		context.no_cache = True
		context.show_sidebar = True
		context.parents = [dict(label='View All Chapters',
			route='chapters', title='View Chapters')]

	def validate(self):
		if not self.route:		#pylint: disable=E0203
			self.route = 'chapters/' + self.scrub(self.name)

	def enable(self):
		chapter = frappe.get_doc('Chapter', frappe.form_dict.name)
		chapter.append('members', dict(enable=self.value))
		chapter.save(ignore_permissions=1)
		frappe.db.commit()


def get_list_context(context):
	context.allow_guest = True
	context.no_cache = True
	context.show_sidebar = True
	context.title = 'All Chapters'
	context.no_breadcrumbs = True
	context.order_by = 'creation desc'


@frappe.whitelist()
def leave(title, user_id, leave_reason):
	chapter = frappe.get_doc("Chapter", title)
	for member in chapter.members:
		if member.user == user_id:
			member.enabled = 0
			member.leave_reason = leave_reason
	chapter.save(ignore_permissions=1)
	frappe.db.commit()
	return "Thank you for Feedback"
