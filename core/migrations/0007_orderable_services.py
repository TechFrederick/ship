# Generated by Django 3.0.7 on 2020-06-26 23:27

from django.db import migrations, models


def fill_in_ordering(apps, schema_editor):
    """Give an ordering value to any existing service or category.

    The ordered model doesn't seem to work when the ordered values are the same.
    Give an incrementing value to each existing row.
    """
    ServiceCategory = apps.get_model("core", "ServiceCategory")
    for order, category in enumerate(
        ServiceCategory.objects.filter(order=0).order_by("id"), start=1
    ):
        category.order = order
        category.save()

    Service = apps.get_model("core", "Service")
    for order, service in enumerate(
        Service.objects.filter(order=0).order_by("id"), start=1
    ):
        service.order = order
        service.save()


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_service_organization_name"),
    ]

    operations = [
        migrations.AlterModelOptions(name="service", options={"ordering": ("order",)},),
        migrations.AlterModelOptions(
            name="servicecategory",
            options={
                "ordering": ("order",),
                "verbose_name_plural": "service categories",
            },
        ),
        migrations.AddField(
            model_name="service",
            name="order",
            field=models.PositiveIntegerField(
                db_index=True, default=0, editable=False, verbose_name="order"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="servicecategory",
            name="order",
            field=models.PositiveIntegerField(
                db_index=True, default=0, editable=False, verbose_name="order"
            ),
            preserve_default=False,
        ),
        migrations.RunPython(fill_in_ordering, migrations.RunPython.noop),
    ]