# Generated by Django 2.2.9 on 2020-10-15 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Symbols',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=7)),
                ('last_refreshed', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='DailyPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('open', models.FloatField()),
                ('high', models.FloatField()),
                ('low', models.FloatField()),
                ('close', models.FloatField()),
                ('symbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Symbols')),
            ],
        ),
    ]
