from test_plus.test import TestCase

from .factories import ServiceFactory, ServiceCategoryFactory


class TestIndex(TestCase):
    def test_ok(self):
        self.get_check_200("core:index")

    def test_has_categories(self):
        """The service categories are rendered on the page."""
        category = ServiceCategoryFactory()

        response = self.get("core:index")

        self.assertContains(response, category.name)


class TestServiceCategoryDetailView(TestCase):
    def test_ok(self):
        category = ServiceCategoryFactory()

        self.get_check_200("core:service-category-detail", slug=category.slug)

    def test_has_services(self):
        """The service category page lists all services."""
        category = ServiceCategoryFactory()
        service = ServiceFactory(category=category)
        ServiceFactory()

        self.get("core:service-category-detail", slug=category.slug)

        services = self.get_context("services")
        assert list(services) == [service]


class TestServiceDetailView(TestCase):
    def test_ok(self):
        service = ServiceFactory()

        self.get_check_200("core:service-detail", pk=service.id)
