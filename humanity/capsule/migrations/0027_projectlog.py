# Generated by Django 3.1.3 on 2020-11-29 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capsule', '0026_delete_projectlog'),
    ]

    operations = [
        migrations.CreateModel(
            name='projectLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('project_id', models.IntegerField()),
                ('log', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
