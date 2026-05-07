import frappe
from frappe import _

def _get_profile_by_name(profile_name):
    if not profile_name:
        return None
    if not frappe.db.exists("NGO Donor Profile", profile_name):
        return None
    return frappe.get_doc("NGO Donor Profile", profile_name)

def _get_profile_by_donor(donor_name):
    if not donor_name:
        return None
    profile_name = frappe.db.get_value("NGO Donor Profile", {"donor": donor_name}, "name")
    if not profile_name:
        return None
    return frappe.get_doc("NGO Donor Profile", profile_name)

def _get_profile_from_donation(donation_name):
    if not donation_name or not frappe.db.exists("Donation", donation_name):
        return None, None

    donation = frappe.get_doc("Donation", donation_name)
    profile = _get_profile_by_donor(donation.donor) if donation.donor else None
    return profile, donation

def _fill_receipt_from_profile(doc, profile, donation=None):
    doc.donor_profile = profile.name
    if profile.donor:
        doc.erpnext_donor = profile.donor
    doc.donor_name = (
        donation.donor_name if donation and donation.donor_name
        else profile.full_name or profile.name
    )
    doc.email = (
        donation.email if donation and donation.email
        else profile.email
    )
    doc.pan_number = profile.pan_number

def _fill_certificate_from_profile(doc, profile, receipt=None, donation=None):
    doc.donor_profile = profile.name
    if profile.donor:
        doc.erpnext_donor = profile.donor
    doc.donor_name = (
        receipt.donor_name if receipt and receipt.donor_name
        else donation.donor_name if donation and donation.donor_name
        else profile.full_name or profile.name
    )
    doc.donor_pan = profile.pan_number

def populate_donation_receipt(doc, method=None):
    profile = None
    donation = None

    if doc.donor_profile:
        profile = _get_profile_by_name(doc.donor_profile)

    if not profile and doc.erpnext_donor:
        profile = _get_profile_by_donor(doc.erpnext_donor)

    if not profile and doc.erpnext_donation:
        profile, donation = _get_profile_from_donation(doc.erpnext_donation)

    if not profile:
        frappe.throw(_("Could not find NGO Donor Profile. Set ERPNext Donation or ERPNext Donor first."))

    _fill_receipt_from_profile(doc, profile, donation=donation)

def populate_donation_certificate(doc, method=None):
    profile = None
    receipt = None
    donation = None

    if doc.donor_profile:
        profile = _get_profile_by_name(doc.donor_profile)

    if not profile and doc.donation_receipt and frappe.db.exists("Donation Receipt", doc.donation_receipt):
        receipt = frappe.get_doc("Donation Receipt", doc.donation_receipt)
        if receipt.donor_profile:
            profile = _get_profile_by_name(receipt.donor_profile)
        if not profile and receipt.erpnext_donor:
            profile = _get_profile_by_donor(receipt.erpnext_donor)

    if not profile and doc.erpnext_donor:
        profile = _get_profile_by_donor(doc.erpnext_donor)

    if not profile and doc.erpnext_donation:
        profile, donation = _get_profile_from_donation(doc.erpnext_donation)

    if not profile:
        frappe.throw(_("Could not find NGO Donor Profile. Set Donation Receipt, ERPNext Donation, or ERPNext Donor first."))

    _fill_certificate_from_profile(doc, profile, receipt=receipt, donation=donation)