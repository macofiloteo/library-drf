# Generated by Django 3.1 on 2020-08-08 16:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20200808_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='addedDate',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]