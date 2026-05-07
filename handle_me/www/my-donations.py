import frappe
from handle_me.api.donor_portal import get_portal_summary, get_my_donations, get_my_receipts, get_my_certificates

def get_context(context):
    if frappe.session.user == "Guest":
        frappe.local.flags.redirect_location = "/login"
        raise frappe.Redirect

    context.no_cache = 1
    context.title = "My Donations"
    context.summary = get_portal_summary()
    context.donations = get_my_donations()
    context.receipts = get_my_receipts()
    context.certificates = get_my_certificates()