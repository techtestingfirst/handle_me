import frappe
from frappe import _
from frappe.utils import flt, now_datetime

def _get_logged_in_profile():
    if frappe.session.user == "Guest":
        frappe.throw(_("Please login first"), frappe.PermissionError)

    profile_name = frappe.db.get_value(
        "NGO Donor Profile",
        {
            "user": frappe.session.user,
            "portal_enabled": 1
        },
        "name"
    )

    if not profile_name:
        frappe.throw(_("No enabled NGO Donor Profile is linked to this user"), frappe.PermissionError)

    return frappe.get_doc("NGO Donor Profile", profile_name)

def _get_profile_display_name(profile):
    return profile.get("full_name") or profile.get("email") or profile.name

@frappe.whitelist()
def get_portal_summary():
    profile = _get_logged_in_profile()
    donor = profile.get("donor")

    summary = {
        "profile_name": profile.name,
        "full_name": _get_profile_display_name(profile),
        "email": profile.get("email") or frappe.session.user,
        "pan_number": profile.get("pan_number"),
        "donor": donor,
        "donation_count": 0,
        "total_amount": 0,
        "recent_donations": [],
        "recent_receipts": [],
        "recent_certificates": [],
    }

    if donor and frappe.db.exists("DocType", "Donation"):
        donations = frappe.get_all(
            "Donation",
            filters={"donor": donor},
            fields=["name", "date", "amount", "mode_of_payment", "payment_id", "docstatus", "creation"],
            order_by="creation desc"
        )
        summary["donation_count"] = len(donations)
        summary["total_amount"] = sum(flt(d.get("amount")) for d in donations)
        summary["recent_donations"] = donations[:5]

    if frappe.db.exists("DocType", "Donation Receipt"):
        summary["recent_receipts"] = frappe.get_all(
            "Donation Receipt",
            filters={"donor_profile": profile.name},
            fields=[
                "name",
                "receipt_date",
                "amount",
                "status",
                "receipt_pdf",
                "payment_mode",
                "payment_reference",
                "creation"
            ],
            order_by="creation desc",
            limit=5
        )

    if frappe.db.exists("DocType", "Donation Certificate"):
        summary["recent_certificates"] = frappe.get_all(
            "Donation Certificate",
            filters={"donor_profile": profile.name},
            fields=[
                "name",
                "certificate_type",
                "financial_year",
                "issue_date",
                "status",
                "file",
                "donor_download_enabled",
                "creation"
            ],
            order_by="creation desc",
            limit=5
        )

    return summary

@frappe.whitelist()
def get_my_donations():
    profile = _get_logged_in_profile()
    donor = profile.get("donor")

    if not donor or not frappe.db.exists("DocType", "Donation"):
        return []

    return frappe.get_all(
        "Donation",
        filters={"donor": donor},
        fields=["name", "date", "amount", "mode_of_payment", "payment_id", "docstatus", "creation"],
        order_by="creation desc"
    )

@frappe.whitelist()
def get_my_receipts():
    profile = _get_logged_in_profile()

    if not frappe.db.exists("DocType", "Donation Receipt"):
        return []

    return frappe.get_all(
        "Donation Receipt",
        filters={"donor_profile": profile.name},
        fields=[
            "name",
            "receipt_date",
            "amount",
            "status",
            "receipt_pdf",
            "payment_mode",
            "payment_reference",
            "erpnext_donor",
            "erpnext_donation",
            "creation"
        ],
        order_by="creation desc"
    )

@frappe.whitelist()
def get_my_certificates():
    profile = _get_logged_in_profile()

    if not frappe.db.exists("DocType", "Donation Certificate"):
        return []

    return frappe.get_all(
        "Donation Certificate",
        filters={"donor_profile": profile.name},
        fields=[
            "name",
            "certificate_type",
            "financial_year",
            "issue_date",
            "status",
            "file",
            "donor_download_enabled",
            "donor_download_count",
            "last_downloaded_on",
            "creation"
        ],
        order_by="creation desc"
    )

@frappe.whitelist()
def download_my_certificate(certificate):
    profile = _get_logged_in_profile()
    cert = frappe.get_doc("Donation Certificate", certificate)

    if cert.donor_profile != profile.name and cert.erpnext_donor != profile.donor:
        frappe.throw(_("You are not allowed to download this certificate"), frappe.PermissionError)

    if not cert.donor_download_enabled:
        frappe.throw(_("Download is disabled for this certificate"), frappe.PermissionError)

    if not cert.file:
        frappe.throw(_("No file is attached to this certificate"))

    frappe.db.set_value(
        "Donation Certificate",
        cert.name,
        {
            "donor_download_count": flt(cert.donor_download_count or 0) + 1,
            "last_downloaded_on": now_datetime()
        },
        update_modified=False
    )

    file_name = frappe.db.get_value(
        "File",
        {
            "file_url": cert.file,
            "attached_to_doctype": "Donation Certificate",
            "attached_to_name": cert.name
        },
        "name"
    )

    if file_name:
        file_doc = frappe.get_doc("File", file_name)
        frappe.response.filename = file_doc.file_name or f"{cert.name}.pdf"
        frappe.response.filecontent = file_doc.get_content()
        frappe.response.type = "download"
        frappe.response.display_content_as = "attachment"
        return

    frappe.local.response["type"] = "redirect"
    frappe.local.response["location"] = cert.file