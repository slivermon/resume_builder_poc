# Generated by Django 5.0.6 on 2024-06-11 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume_builder', '0003_alter_timeline_event_detail_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeline_event_detail',
            name='degree',
        ),
    ]
