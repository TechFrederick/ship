import factory


class ServiceCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "core.ServiceCategory"

    name = factory.Sequence(lambda n: f"Service Category {n}")
    slug = factory.Sequence(lambda n: f"service-category-{n}")
    description = factory.Faker("sentence")
    icon = "categories/shelter.png"


class ServiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "core.Service"

    name = factory.Sequence(lambda n: f"Service {n}")
    description = factory.Faker("paragraph")
    website = factory.Faker("url")
    street_address = factory.Faker("street_address")
    city = factory.Faker("city")
    state = factory.Faker("state_abbr")
    zip_code = factory.Faker("postcode")
    latitude = factory.Faker("latitude")
    longitude = factory.Faker("longitude")
    operating_hours = "9am - 5pm Monday-Friday"
    phone_number = factory.Faker("phone_number")
    email = factory.Faker("email")
    category = factory.SubFactory(ServiceCategoryFactory)
