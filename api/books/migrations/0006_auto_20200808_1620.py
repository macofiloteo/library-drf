# Generated by Django 3.1 on 2020-08-08 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20200808_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='checkOutDate',
            field=models.DateTimeField(),
        ),
    ]
