from handle_me.api.donor_portal import (
    get_my_certificates,
    get_my_donations,
    get_my_receipts,
    get_portal_summary,
    redirect_guest_to_login,
)


def get_context(context):
    redirect_guest_to_login()
    context.no_cache = 1
    context.title = "My Donations"
    context.summary = get_portal_summary()
    context.donations = get_my_donations()
    context.receipts = get_my_receipts()
    context.certificates = get_my_certificates()
