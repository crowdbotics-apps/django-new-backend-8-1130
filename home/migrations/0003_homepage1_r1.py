# Generated by Django 2.2.7 on 2019-11-27 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_homepage1"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage1",
            name="r1",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="homepage1_r1",
                to="home.HomePage",
            ),
        ),
    ]
