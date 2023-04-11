## в файл `__init__.py` добавить следующие строчки

```python
default_app_config = 'post.apps.PostConfig'
```

## если наш `models.py` условно выглядит таким образом

```python
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(
        User, related_name='posts', on_delete=models.CASCADE
    )
    title = models.CharField(max_length=55)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=False, blank=True)

    def __str__(self):
        return f"{self.author} -> {self.title}"

```

## то необходимо создать файл `signals.py`

```python
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
```

## и в `apps.py` добавить 

```python
from django.apps import AppConfig
from django.db.models.signals import pre_save

class PostConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'post'

    def ready(self):
        import post.signals
        pre_save.connect(post.signals.add_created_at, sender=post.models.Post)
```

## поле `created_at` будет автоматически заполняться текущим временем, если пользователь не заполнил его