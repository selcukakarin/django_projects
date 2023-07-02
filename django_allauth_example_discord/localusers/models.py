from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# AbstractBaseUser'da burada kullanılabilirdi. Fakat bu AbstractBaseUser daha fazla özellik barındırmaktadır.
class LocalUser(AbstractUser):
    pass