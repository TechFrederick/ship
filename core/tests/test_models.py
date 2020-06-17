from test_plus.test import TestCase

from core.tests.factories import ServiceCategoryFactory


class TestServiceCategory(TestCase):
    def test_factory(self):
        category = ServiceCategoryFactory()

        assert category.name

    def test_str(self):
        category = ServiceCategoryFactory()

        assert str(category) == category.name
