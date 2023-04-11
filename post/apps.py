from django.apps import AppConfig
from django.db.models.signals import pre_save

class PostConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'post'

    def ready(self):
        import post.signals
        pre_save.connect(post.signals.add_created_at, sender=post.models.Post)