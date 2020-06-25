from django.db import models


class ServiceCategory(models.Model):
    """Each service must belong to a category for easy browsing."""

    name = models.CharField(max_length=128)
    slug = models.SlugField(
        help_text="This is the unique name that will display in the URL."
    )
    description = models.TextField(default="")
    icon = models.CharField(
        max_length=128,
        help_text=(
            "Upload a 300px x 300px to the 'static' directory. Add file path here."
        ),
        default="",
    )
    COLOR_CHOICES = (
        ("red", "Red"),
        ("teal", "Teal"),
        ("orange", "Orange"),
        ("purple", "Purple"),
        ("green", "Green"),
        ("indigo", "Indigo"),
        ("yellow", "Yellow"),
        ("gray", "Gray"),
    )
    color = models.CharField(max_length=8, choices=COLOR_CHOICES, default="gray")

    class Meta:
        verbose_name_plural = "service categories"

    def __str__(self):
        return self.name


class Service(models.Model):
    """A community service that is available to homeless citizens."""

    name = models.CharField(max_length=128)
    organization_name = models.CharField(max_length=128, default="")
    description = models.TextField()
    website = models.URLField(default="", blank=True)

    street_address = models.CharField(max_length=256, default="")
    city = models.CharField(max_length=128, default="")
    state = models.CharField(max_length=32, default="")
    zip_code = models.CharField(max_length=16, default="")
    latitude = models.CharField(max_length=16, default="", blank=True)
    longitude = models.CharField(max_length=16, default="", blank=True)

    operating_hours = models.CharField(max_length=256, blank=True)
    phone_number = models.CharField(max_length=32, blank=True)
    email = models.EmailField(blank=True)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
