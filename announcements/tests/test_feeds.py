import datetime

from django.utils import timezone
from test_plus.test import TestCase

from .factories import AnnouncementFactory


class TestAnnouncementFeed(TestCase):
    def test_ok(self):
        announcement = AnnouncementFactory()

        response = self.get("announcements:feed")

        self.assertResponseContains(announcement.title, response, html=False)
        self.assertResponseContains(announcement.description, response, html=False)

    def test_limit_items(self):
        """A limited number of items is in the feed."""
        AnnouncementFactory(
            title="Not going to be there",
            expires_at=timezone.now() - datetime.timedelta(days=1),
        )
        for i in range(5):
            AnnouncementFactory()

        response = self.get("announcements:feed")

        assert "Not going to be there" not in response.content.decode()
