import datetime

from django.utils import timezone
from test_plus.test import TestCase

from announcements.models import Announcement
from announcements.tests.factories import AnnouncementFactory


class TestAnnouncement(TestCase):
    def test_factory(self):
        announcement = AnnouncementFactory()

        assert announcement.title
        assert announcement.description
        assert announcement.expires_at

    def test_str(self):
        announcement = AnnouncementFactory()

        assert str(announcement) == announcement.title

    def test_ordering(self):
        now = timezone.now()
        original_announcement = AnnouncementFactory(
            expires_at=now + datetime.timedelta(days=7)
        )
        newest_announcement = AnnouncementFactory(
            expires_at=now + datetime.timedelta(days=14)
        )
        newer_announcement = AnnouncementFactory(
            expires_at=now + datetime.timedelta(days=10)
        )

        announcements = Announcement.objects.all()

        assert list(announcements) == [
            newest_announcement,
            newer_announcement,
            original_announcement,
        ]
