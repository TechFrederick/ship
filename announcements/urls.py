from django.urls import path

from . import views

app_name = "announcements"
urlpatterns = [
    path("<int:pk>/", views.AnnouncementDetailView.as_view(), name="detail"),
]
