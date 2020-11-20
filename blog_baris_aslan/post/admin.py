from django.contrib import admin
from .models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'publishingDate', 'slug']
    list_display_links = ['publishingDate']
    list_filter = ['publishingDate']
    search_fields = ['title', 'content']
    list_editable = ['title']


    class Meta:
        model = Post

admin.site.register(Post,PostAdmin)