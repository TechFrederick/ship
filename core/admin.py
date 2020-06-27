from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from .models import Service, ServiceCategory


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(OrderedModelAdmin):
    list_display = ("name", "move_up_down_links")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Service)
class ServiceAdmin(OrderedModelAdmin):
    list_display = ("name", "organization_name", "category", "move_up_down_links")
    ordering = ["category", "order"]
