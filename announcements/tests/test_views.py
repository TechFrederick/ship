from test_plus.test import TestCase

from .factories import AnnouncementFactory


class TestAnnouncementDetailView(TestCase):
    def test_ok(self):
        announcement = AnnouncementFactory()

        self.get_check_200("announcements:detail", pk=announcement.id)
