# Generated by Django 3.0.7 on 2020-06-17 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ServiceCategory",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                (
                    "slug",
                    models.SlugField(
                        help_text=(
                            "This is the unique name that will display in the URL."
                        )
                    ),
                ),
            ],
            options={"verbose_name_plural": "service categories",},
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("description", models.TextField()),
                ("location", models.CharField(max_length=256)),
                ("operating_hours", models.CharField(max_length=256)),
                ("phone_number", models.CharField(max_length=32)),
                ("email", models.EmailField(max_length=254)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.ServiceCategory",
                    ),
                ),
            ],
        ),
    ]
