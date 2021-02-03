from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


def _send_confirmation_email(self, order):
    cust_email = order.email
    subject = render_to_string(
        'checkout/confirmation_emails/confirmation_emails_subject.txt',
        {'order': order})
    body = render_to_string(
        'checkout/confirmation_emails/confirmation_emails_body.txt',
        {'order': order})
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email]
    )
