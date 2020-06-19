from django.db import models


class ServiceCategory(models.Model):
    """Each service must belong to a category for easy browsing."""

    name = models.CharField(max_length=128)
    slug = models.SlugField(
        help_text="This is the unique name that will display in the URL."
    )

    class Meta:
        verbose_name_plural = "service categories"

    def __str__(self):
        return self.name


class Service(models.Model):
    """A community service that is available to homeless citizens."""

    name = models.CharField(max_length=128)
    description = models.TextField()
    website = models.URLField(default="")

    street_address = models.CharField(max_length=256, default="")
    city = models.CharField(max_length=128, default="")
    state = models.CharField(max_length=32, default="")
    zip_code = models.CharField(max_length=16, default="")

    operating_hours = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=32)
    email = models.EmailField()
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
