from django.db import models

# Create your models here.

class Comment(models.Model):
    post_id = models.IntegerField()
    text = models.TextField(max_length=1000)