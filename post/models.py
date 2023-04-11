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
