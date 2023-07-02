from django.contrib import admin
from .models import Article

# Register your models here.

from .forms import Article
 
class ComputerAdmin(admin.ModelAdmin):
   list_display = ["title", "any_date"]
   form = Article
   list_filter = ['title']
   search_fields = ['title']

admin.site.register(Article)