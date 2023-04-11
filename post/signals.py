from django.db import transaction
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Post

@receiver(pre_save, sender=Post)
@transaction.atomic
def add_created_at(sender, instance, **kwargs):
    if not instance.created_at:
        instance.created_at = timezone.now()