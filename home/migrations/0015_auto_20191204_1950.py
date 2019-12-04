# Generated by Django 2.2.7 on 2019-12-04 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_rx3_r2'),
    ]

    operations = [
        migrations.AddField(
            model_name='rx3',
            name='r3',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=30, null=True),
        ),
        migrations.AddField(
            model_name='rx3',
            name='r4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rx3_r4', to='home.CustomText'),
        ),
    ]
