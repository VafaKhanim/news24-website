from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import News, Subscribe


@receiver(post_save, sender=News)
def news_notification(sender, instance, created, **kwargs):
    if created:
        subject = f"New Article Published: {instance.title}"
        message = f"Dear Subscriber,\n\nWe are excited to inform you that a new article titled '{instance.title}' has been published on our website.\n\nStay updated with the latest news!"
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [sub.email for sub in Subscribe.objects.all()]

        if recipient_list:
            send_mail(subject, message, from_email, recipient_list)


# Yeni istifadəçi abunə olduqda təşəkkür mesajı göndərmək
@receiver(post_save, sender=Subscribe)
def news_subscriber(sender, instance, created, **kwargs):
    if created:
        subject = "Thanks for joining us!"
        message = "Hello,\n\nThank you for subscribing to our news website. We appreciate your interest!"
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [instance.email]

        # E-poçtu göndəririk
        try:
            send_mail(subject, message, from_email, recipient_list)
        except Exception as e:
            print(f"Email sending error: {e}")