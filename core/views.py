from django.shortcuts import render
from django.views.generic import ListView

from .models import ServiceCategory


class IndexView(ListView):
    queryset = ServiceCategory.objects.all()
    template_name = "core/index.html"
