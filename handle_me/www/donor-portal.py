from handle_me.api.donor_portal import get_portal_summary, redirect_guest_to_login


def get_context(context):
    redirect_guest_to_login()
    context.no_cache = 1
    context.title = "Donor Portal"
    context.summary = get_portal_summary()
