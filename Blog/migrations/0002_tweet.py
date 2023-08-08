# Generated by Django 4.2.3 on 2023-07-19 00:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("Blog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tweet",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cuerpo", models.TextField(max_length=250)),
                ("fecha", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]