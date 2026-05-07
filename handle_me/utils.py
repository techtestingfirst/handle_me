# apps/handle_me/handle_me/utils.py
import frappe

def get_website_user_home_page(user):
    if "Donor" in frappe.get_roles(user):
        return "/donor-portal"
    return "/me"