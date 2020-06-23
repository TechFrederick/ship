from test_plus.test import TestCase

from core.tests.factories import ServiceFactory, ServiceCategoryFactory


class TestServiceCategory(TestCase):
    def test_factory(self):
        category = ServiceCategoryFactory()

        assert category.name
        assert category.slug

    def test_str(self):
        category = ServiceCategoryFactory()

        assert str(category) == category.name


class TestService(TestCase):
    def test_factory(self):
        service = ServiceFactory()

        assert service.name
        assert service.description
        assert service.website
        assert service.street_address
        assert service.city
        assert service.state
        assert service.zip_code
        assert service.latitude
        assert service.longitude
        assert service.operating_hours
        assert service.phone_number
        assert service.email
        assert service.category

    def test_str(self):
        service = ServiceFactory()

        assert str(service) == service.name
