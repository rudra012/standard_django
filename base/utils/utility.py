import sys

from django.conf import settings


def get_base_email_context(request):
    base_email_context = {
        "app_name": settings.APP_NAME,
        # "site_email_logo": (settings.HTTP or "http") + "://" + host + settings.STATIC_URL + "front/dist/img/logo.png",
    }
    print(base_email_context)
    return base_email_context


def email_send(subject, message, to_email_list, attachment=None, attachment_name="", attachment_type=""):
    from django.core.mail import EmailMessage

    bcc = ['rudra12shailesh@gmail.com', ]
    # bcc = get_bcc_emails()
    from_email = settings.EMAIL_HOST_USER
    print(bcc)
    try:
        email = EmailMessage(subject, message, to=to_email_list, from_email=from_email, bcc=bcc)
        if attachment:
            email.attach('{}'.format(attachment_name), attachment, '{}'.format(attachment_type))
        email.content_subtype = 'html'
        email.send()
    except:
        if settings.DEBUG:
            print("email_send: ", sys.exc_info())


def mass_email_send(emails):
    from django.core import mail

    try:
        mail.send_mass_mail(emails)
    except:
        if settings.DEBUG:
            print("mass_email_send: ", sys.exc_info())
