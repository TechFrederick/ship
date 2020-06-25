from django.contrib.syndication.views import Feed
from django.urls import reverse

from .models import Announcement


class AnnouncementFeed(Feed):
    """Generate an RSS feed that Mailchimp (or any feed reader) can import."""

    title = "Announcement from SHIP"
    description = "Announcements for homeless in Frederick County, Maryland"

    @property
    def link(self):
        return reverse("announcements:list")

    def items(self):
        return Announcement.objects.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return reverse("announcements:list") + f"#announcement-{item.id}"
