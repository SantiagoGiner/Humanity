# Generated by Django 3.1.3 on 2020-11-29 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capsule', '0023_remove_projectlog_project_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='projectLog',
        ),
    ]
