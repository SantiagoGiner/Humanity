# Generated by Django 3.1.4 on 2020-12-08 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capsule', '0040_auto_20201208_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_photo',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]
