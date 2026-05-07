import frappe
from handle_me.api.donor_portal import get_portal_summary

def get_context(context):
    if frappe.session.user == "Guest":
        frappe.local.flags.redirect_location = "/login"
        raise frappe.Redirect

    context.no_cache = 1
    context.title = "Donor Portal"
    context.summary = get_portal_summary()