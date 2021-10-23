from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.conf import settings

from BiaBegard.tasks import async_send_email
from .models import Blog
from account.models import Subscribers


@receiver(post_save, sender=Blog)
def create_price_history(sender, instance: Blog, created, **kwargs):
    if created:
        if instance.active:
            mail_subject = instance.title
            message = render_to_string('bekhon.html', {
                'blog': instance,
                'my_domain': settings.MY_DOMAIN
            })
            q = Subscribers.objects.filter(active=True).values('email')
            emails = [email['email'] for email in q]
            async_send_email.delay(mail_subject, message, emails)
