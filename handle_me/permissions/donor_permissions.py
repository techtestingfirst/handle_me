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


def _profile_query(doctype, user=None):
    user = _get_user(user)
    if _is_privileged_user(user):
        return ""
    donor_profile = _get_donor_profile_name(user)
    if not donor_profile:
        return "1=0"
    return f"`tab{doctype}`.`donor_profile` = {_escape(donor_profile)}"


def _profile_has_permission(doc, ptype, allowed_ptypes, user=None):
    user = _get_user(user)
    privileged = _allow_if_privileged(user)
    if privileged is None:
        return None
    donor_profile = _get_donor_profile_name(user)
    if not donor_profile:
        return False
    return ptype in allowed_ptypes and doc.donor_profile == donor_profile


def _user_query(doctype, user=None):
    user = _get_user(user)
    if _is_privileged_user(user):
        return ""
    if user == "Guest":
        return "1=0"
    return f"`tab{doctype}`.`user` = {_escape(user)}"


def _user_has_permission(doc, ptype, allowed_ptypes, user=None):
    user = _get_user(user)
    privileged = _allow_if_privileged(user)
    if privileged is None:
        return None
    if user == "Guest":
        return False
    return ptype in allowed_ptypes and doc.user == user


def ngo_donor_profile_query(user=None, doctype=None):
    return _user_query("NGO Donor Profile", user)


def ngo_donor_profile_has_permission(doc, ptype="read", user=None):
    return _user_has_permission(doc, ptype, ("read", "write", "print", "email"), user)


def donation_intent_query(user=None, doctype=None):
    return _profile_query("Donation Intent", user)


def donation_intent_has_permission(doc, ptype="read", user=None):
    return _profile_has_permission(doc, ptype, ("read", "write", "create", "print", "email"), user)


def donation_receipt_query(user=None, doctype=None):
    return _profile_query("Donation Receipt", user)


def donation_receipt_has_permission(doc, ptype="read", user=None):
    return _profile_has_permission(doc, ptype, ("read", "print", "email"), user)


def donation_certificate_query(user=None, doctype=None):
    return _profile_query("Donation Certificate", user)


def donation_certificate_has_permission(doc, ptype="read", user=None):
    return _profile_has_permission(doc, ptype, ("read", "print", "email"), user)


def donor_consent_log_query(user=None, doctype=None):
    return _profile_query("Donor Consent Log", user)


def donor_consent_log_has_permission(doc, ptype="read", user=None):
    return _profile_has_permission(doc, ptype, ("read",), user)


def portal_access_log_query(user=None, doctype=None):
    return _user_query("Portal Access Log", user)


def portal_access_log_has_permission(doc, ptype="read", user=None):
    return _user_has_permission(doc, ptype, ("read",), user)


def donor_communication_log_query(user=None, doctype=None):
    return _profile_query("Donor Communication Log", user)


def donor_communication_log_has_permission(doc, ptype="read", user=None):
    return _profile_has_permission(doc, ptype, ("read",), user)
