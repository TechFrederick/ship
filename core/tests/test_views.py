from test_plus.test import TestCase

from .factories import ServiceCategoryFactory


class TestIndex(TestCase):
    def test_ok(self):
        self.get_check_200("core:index")

    def test_has_categories(self):
        """The service categories are rendered on the page."""
        category = ServiceCategoryFactory()

        response = self.get("core:index")

        self.assertContains(response, category.name)
