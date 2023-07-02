from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50)
    any_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)

    def __str__(self):
        return self.title