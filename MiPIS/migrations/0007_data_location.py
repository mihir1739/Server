# Generated by Django 4.0.1 on 2022-05-23 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiPIS', '0006_data_found'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='location',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
