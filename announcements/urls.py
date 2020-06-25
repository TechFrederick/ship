from django.urls import path

from . import feeds, views

app_name = "announcements"
urlpatterns = [
    path("", views.AnnouncementListView.as_view(), name="list"),
    path("feed/", feeds.AnnouncementFeed(), name="feed"),
]
