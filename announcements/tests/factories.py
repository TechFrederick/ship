import datetime

import factory
from django.utils import timezone


class AnnouncementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "announcements.Announcement"

    title = factory.Faker("sentence")
    description = factory.Faker("paragraph")
    expires_at = factory.LazyFunction(
        lambda: timezone.now() + datetime.timedelta(days=14)
    )
