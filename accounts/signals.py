from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User

@receiver(post_save, sender=User)
def set_superuser_role(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        User.objects.filter(pk=instance.pk).update(role='SUPERADMIN')
