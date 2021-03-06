# Generated by Django 3.1.3 on 2020-11-26 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capsule', '0015_delete_goal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('priority', models.CharField(default='daily', max_length=9)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
