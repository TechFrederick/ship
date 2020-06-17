from django.db import models


class ServiceCategory(models.Model):
    """Each service must belong to a category for easy browsing."""

    name = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = "service categories"

    def __str__(self):
        return self.name
