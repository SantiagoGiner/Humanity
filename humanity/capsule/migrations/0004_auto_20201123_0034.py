# Generated by Django 3.1.3 on 2020-11-23 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capsule', '0003_auto_20201122_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]
