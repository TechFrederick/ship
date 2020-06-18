from django.contrib import admin

from .models import Announcement


@admin.register(Announcement)
class AnnouncementModelAdmin(admin.ModelAdmin):
    list_display = ("title", "expires_at")
    date_hierarchy = "expires_at"
