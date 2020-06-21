from django.views.generic import DetailView

from .models import Announcement


class AnnouncementDetailView(DetailView):
    model = Announcement
