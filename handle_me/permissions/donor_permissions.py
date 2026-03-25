import frappe

SYSTEM_ROLES = {
    "System Manager",
    "NGO Admin",
    "Accounts User",
    "Program Manager",
    "Compliance Officer",
}

def _is_privileged_user(user=None):
    user = user or frappe.session.user
    if not user or user in ("Administrator", "Guest"):
        return user == "Administrator"
    roles = set(frappe.get_roles(user))
    return bool(roles & SYSTEM_ROLES)

def _get_user(user=None):
    return user or frappe.session.user

def _get_donor_profile_name(user=None):
    user = _get_user(user)
    if not user or user == "Guest":
        return None
    return frappe.db.get_value("NGO Donor Profile", {"user": user}, "name")

def _get_donor_name(user=None):
    profile = _get_donor_profile_name(user)
    if not profile:
        return None
    return frappe.db.get_value("NGO Donor Profile", profile, "donor")

def _escape(value):
    return frappe.db.escape(value)

def _allow_if_privileged(user=None):
    return None if _is_privileged_user(user) else False

def ngo_donor_profile_query(user=None, doctype=None):
    user = _get_user(user)
    if _is_privileged_user(user):
        return ""
    if user == "Guest":
        return "1=0"
    return f"`tabNGO Donor Profile`.`user` = {_escape(user)}"

def ngo_donor_profile_has_permission(doc, ptype="read", user=None):
    user = _get_user(user)
    privileged = _allow_if_privileged(user)
    if privileged is None:
        return None
    if user == "Guest":
        return False
    if ptype in ("read", "write", "print", "email"):
        return doc.user == user
    return False

def donation_intent_query(user=None, doctype=None):
    user = _get_user(user)
    if _is_privileged_user(user):
        return ""
    donor_profile = _get_donor_profile_name(user)
    if not donor_profile:
        return "1=0"
    return f"`tabDonation Intent`.`donor_profile` = {_escape(donor_profile)}"

def donation_intent_has_permission(doc, ptype="read", user=None):
    user = _get_user(user)
    privileged = _allow_if_privileged(user)
    if privileged is None:
        return None
    donor_profile = _get_donor_profile_name(user)
    if not donor_profile:
        return False
    if ptype in ("read", "write", "create", "print", "email"):
        return doc.donor_profile == donor_profile
    return False

def donation_receipt_query(user=None, doctype=None):
    user = _get_user(user)
    if _is_privileged_user(user):
        return ""
    donor_profile = _get_donor_profile_name(user)
    if not donor_profile:
        return "1=0"
    return f"`tabDonation Receipt`.`donor_profile` = {_escape(donor_profile)}"

def donation_receipt_has_permission(doc, ptype="read", user=None):
    user = _get_user(user)
    privileged = _allow_if_privileged(user)
    if privileged is None:
        return None
    donor_profile = _get_donor_profile_name(user)
    if not donor_profile:
        return False
    if ptype in ("read", "print", "email"):
        return doc.donor_profile == donor_profile
    return False

def donation_certificate_query(user=None, doctype=None):
    user = _get_user(user)
    if _is_privileged_user(user):
        return ""
    donor_profile = _get_donor_profile_name(user)
    if not donor_profile:
        return "1=0"
    return f"`tabDonation Certificate`.`donor_profile` = {_escape(donor_profile)}"

def donation_certificate_has_permission(doc, ptype="read", user=None):
    user = _get_user(user)
    privileged = _allow_if_privileged(user)
    if privileged is None:
        return None
    donor_profile = _get_donor_profile_name(user)
    if not donor_profile:
        return False
    if ptype in ("read", "print", "email"):
        return doc.donor_profile == donor_profile
    return False

def donor_consent_log_query(user=None, doctype=None):
    user = _get_user(user)
    if _is_privileged_user(user):
        return ""
    donor_profile = _get_donor_profile_name(user)
    if not donor_profile:
        return "1=0"
    return f"`tabDonor Consent Log`.`donor_profile` = {_escape(donor_profile)}"

def donor_consent_log_has_permission(doc, ptype="read", user=None):
    user = _get_user(user)
    privileged = _allow_if_privileged(user)
    if privileged is None:
        return None
    donor_profile = _get_donor_profile_name(user)
    if not donor_profile:
        return False
    return ptype == "read" and doc.donor_profile == donor_profile

def portal_access_log_query(user=None, doctype=None):
    user = _get_user(user)
    if _is_privileged_user(user):
        return ""
    return f"`tabPortal Access Log`.`user` = {_escape(user)}" if user != "Guest" else "1=0"

def portal_access_log_has_permission(doc, ptype="read", user=None):
    user = _get_user(user)
    privileged = _allow_if_privileged(user)
    if privileged is None:
        return None
    return ptype == "read" and doc.user == user

def donor_communication_log_query(user=None, doctype=None):
    user = _get_user(user)
    if _is_privileged_user(user):
        return ""
    donor_profile = _get_donor_profile_name(user)
    if not donor_profile:
        return "1=0"
    return f"`tabDonor Communication Log`.`donor_profile` = {_escape(donor_profile)}"

def donor_communication_log_has_permission(doc, ptype="read", user=None):
    user = _get_user(user)
    privileged = _allow_if_privileged(user)
    if privileged is None:
        return None
    donor_profile = _get_donor_profile_name(user)
    if not donor_profile:
        return False
    return ptype == "read" and doc.donor_profile == donor_profile
