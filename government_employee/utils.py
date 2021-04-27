from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


def send_tender_winner_holder_email(winner_tender, winner_username, email):
    context = {
        'subject': _('You Are Tender Winner'),
        'winner_tender': winner_tender,
        'winner_username': winner_username,
    }
    html_content = render_to_string(f'government_employee/notice_send/notice_email.html', context)
    text_content = render_to_string(f'government_employee/notice_send/notice_email.txt', context)

    msg = EmailMultiAlternatives(context['subject'], text_content, settings.DEFAULT_FROM_EMAIL, [email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
