from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import PostCategory, SubscribersCategory, User


@receiver(m2m_changed, sender=PostCategory)
def notify_subscribers(sender, instance,  **kwargs):
    subject = f'''Новый пост: "{instance.title}"'''
    if kwargs['action'] == 'post_add':
        subs = list(SubscribersCategory.objects.filter(category__in=instance.category.all()).values('subscribers', 'subscribers__email'))
        emails = []
        for sub in subs:
            emails.append(sub['subscribers__email'])
        for email in emails:
            send_mail(
                from_email='sohuga55@yandex.ru',
                subject=subject,
                message=instance.text[:50] + f'http://127.0.0.1:8000/post/{instance.pk}',
                recipient_list=[email],
            )
        print('instance', instance)
        print('subject', subject)
