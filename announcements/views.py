from django.utils import timezone
from django.views.generic import ListView

from .models import Announcement


class AnnouncementListView(ListView):
    def get_queryset(self):
        return Announcement.objects.filter(expires_at__gte=timezone.now())
