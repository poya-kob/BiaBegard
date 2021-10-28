from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def async_send_email(subject, message, email_list):
    send_mail(subject, message, settings.EMAIL_HOST_USER, email_list)

