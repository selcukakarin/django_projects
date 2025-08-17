from django.contrib import admin
from .models import Article,Comment
from django.contrib.auth.models import Group
from .forms import GroupAdminForm

# Register your models here.
# admin.site.register(Article)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=["title","author","created_date"]
    list_display_links=["title","created_date"]
    search_fields=["title"]
    list_filter=["title","created_date"]
    class Meta:
        model=Article

admin.site.register(Comment)

# Unregister the original Group admin.
admin.site.unregister(Group)

# Create a new Group admin.
class GroupAdmin(admin.ModelAdmin):
    # Use our custom form.
    form = GroupAdminForm
    # Filter permissions horizontal as well.
    filter_horizontal = ['permissions']

# Register the new Group ModelAdmin.
admin.site.register(Group, GroupAdmin)