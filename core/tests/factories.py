import factory


class ServiceCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "core.ServiceCategory"

    name = factory.Sequence(lambda n: f"Service Category {n}")
    slug = factory.Sequence(lambda n: f"service-category-{n}")


class ServiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "core.Service"

    name = factory.Sequence(lambda n: f"Service {n}")
    description = factory.Faker("paragraph")
    location = factory.Faker("address")
    operating_hours = "9am - 5pm Monday-Friday"
    phone_number = factory.Faker("phone_number")
    email = factory.Faker("email")
    category = factory.SubFactory(ServiceCategoryFactory)
