import factory


class ServiceCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "core.ServiceCategory"

    name = factory.Sequence(lambda n: f"Service Category {n}")
