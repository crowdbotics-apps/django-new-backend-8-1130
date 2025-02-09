# Generated by Django 2.2.7 on 2019-11-27 19:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("home", "0003_homepage1_r1"),
    ]

    operations = [
        migrations.CreateModel(
            name="NursingInstruction",
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
                ("name", models.CharField(max_length=255)),
                ("key_word", models.CharField(blank=True, max_length=255)),
                (
                    "r3",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="nursinginstruction_r3",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
