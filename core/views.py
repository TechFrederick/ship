from django.views.generic import DetailView, ListView
from django.utils import timezone

from announcements.models import Announcement

from .models import Service, ServiceCategory


class IndexView(ListView):
    queryset = ServiceCategory.objects.all()
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["announcements"] = Announcement.objects.filter(
            expires_at__gte=timezone.now()
        )
        return context


class ServiceCategoryDetailView(DetailView):
    model = ServiceCategory

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.filter(category=self.object)
        return context


class ServiceDetailView(DetailView):
    queryset = Service.objects.all().select_related("category")
