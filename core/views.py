from django.views.generic import DetailView, ListView

from .models import Service, ServiceCategory


class IndexView(ListView):
    queryset = ServiceCategory.objects.all()
    template_name = "core/index.html"


class ServiceCategoryDetailView(DetailView):
    model = ServiceCategory

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.filter(category=self.object)
        return context


class ServiceDetailView(DetailView):
    model = Service
