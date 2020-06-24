import datetime

from django.utils import timezone
from test_plus.test import TestCase

from .factories import AnnouncementFactory


class TestAnnouncementListView(TestCase):
    def test_ok(self):
        AnnouncementFactory()

        self.get_check_200("announcements:list")

    def test_excludes_expired_announcements(self):
        """Old announcements are not included on the page."""
        AnnouncementFactory(expires_at=timezone.now() - datetime.timedelta(days=1))

        self.get("announcements:list")

        announcements = self.get_context("announcement_list")
        assert list(announcements) == []
