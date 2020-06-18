from django.urls import path

from . import views

app_name = "core"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path(
        "category/<slug:slug>/",
        views.ServiceCategoryDetailView.as_view(),
        name="service-category-detail",
    ),
    path(
        "service/<int:pk>/", views.ServiceDetailView.as_view(), name="service-detail",
    ),
]
