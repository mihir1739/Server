# Generated by Django 4.0.1 on 2022-05-17 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiPIS', '0004_remove_data_uid_alter_data_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='accuracy',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='data',
            name='similiar',
            field=models.ImageField(blank=True, upload_to='images/users/'),
        ),
        migrations.AlterField(
            model_name='data',
            name='picture',
            field=models.ImageField(upload_to='images/staff/'),
        ),
    ]
