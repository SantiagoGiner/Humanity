# Generated by Django 3.1.4 on 2020-12-04 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capsule', '0029_library'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Library',
            new_name='Book',
        ),
    ]
