from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.utils import timezone
from django.utils.text import slugify

from post.models import Post


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=120)

    def __str__(self):
        return self.user.username