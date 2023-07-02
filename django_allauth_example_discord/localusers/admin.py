from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import LocalUser

# Register your models here.
admin.site.register(LocalUser, UserAdmin)
