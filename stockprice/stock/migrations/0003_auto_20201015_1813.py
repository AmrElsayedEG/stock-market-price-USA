# Generated by Django 2.2.9 on 2020-10-15 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20201015_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symbols',
            name='last_refreshed',
            field=models.DateField(blank=True, null=True),
        ),
    ]
