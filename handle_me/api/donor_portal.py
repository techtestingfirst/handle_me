import frappe
from frappe import _
from frappe.utils import flt, now_datetime

RECENT_ORDER = "creation desc"
DONATION_FIELDS = ["name", "date", "amount", "mode_of_payment", "payment_id", "docstatus", "creation"]
RECEIPT_FIELDS = [
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
]
CERTIFICATE_FIELDS = [
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
]
RECENT_RECEIPT_FIELDS = [
    "name",
    "receipt_date",
    "amount",
    "status",
    "receipt_pdf",
    "payment_mode",
    "payment_reference",
    "creation"
]
RECENT_CERTIFICATE_FIELDS = [
    "name",
    "certificate_type",
    "financial_year",
    "issue_date",
    "status",
    "file",
    "donor_download_enabled",
    "creation"
]


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


def _get_records(doctype, filters, fields, limit=None):
    if not frappe.db.exists("DocType", doctype):
        return []

    kwargs = {
        "filters": filters,
        "fields": fields,
        "order_by": RECENT_ORDER
    }
    if limit is not None:
        kwargs["limit"] = limit

    return frappe.get_all(doctype, **kwargs)


def _get_donations(profile, limit=None):
    donor = profile.get("donor")
    if not donor:
        return []
    return _get_records("Donation", {"donor": donor}, DONATION_FIELDS, limit=limit)


def _get_receipts(profile, fields=None, limit=None):
    return _get_records(
        "Donation Receipt",
        {"donor_profile": profile.name},
        fields or RECEIPT_FIELDS,
        limit=limit
    )


def _get_certificates(profile, fields=None, limit=None):
    return _get_records(
        "Donation Certificate",
        {"donor_profile": profile.name},
        fields or CERTIFICATE_FIELDS,
        limit=limit
    )


def redirect_guest_to_login():
    if frappe.session.user == "Guest":
        frappe.local.flags.redirect_location = "/login"
        raise frappe.Redirect


@frappe.whitelist()
def get_portal_summary():
    profile = _get_logged_in_profile()

    summary = {
        "profile_name": profile.name,
        "full_name": _get_profile_display_name(profile),
        "email": profile.get("email") or frappe.session.user,
        "pan_number": profile.get("pan_number"),
        "donor": profile.get("donor"),
        "donation_count": 0,
        "total_amount": 0,
        "recent_donations": [],
        "recent_receipts": [],
        "recent_certificates": [],
    }

    donations = _get_donations(profile)
    summary["donation_count"] = len(donations)
    summary["total_amount"] = sum(flt(d.get("amount")) for d in donations)
    summary["recent_donations"] = donations[:5]
    summary["recent_receipts"] = _get_receipts(profile, fields=RECENT_RECEIPT_FIELDS, limit=5)
    summary["recent_certificates"] = _get_certificates(
        profile,
        fields=RECENT_CERTIFICATE_FIELDS,
        limit=5
    )

    return summary


@frappe.whitelist()
def get_my_donations():
    profile = _get_logged_in_profile()
    return _get_donations(profile)


@frappe.whitelist()
def get_my_receipts():
    profile = _get_logged_in_profile()
    return _get_receipts(profile)


@frappe.whitelist()
def get_my_certificates():
    profile = _get_logged_in_profile()
    return _get_certificates(profile)


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
