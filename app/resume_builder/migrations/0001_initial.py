# Generated by Django 5.0.6 on 2024-06-10 23:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Timeline_Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_add_datetime', models.DateTimeField(verbose_name='datetime event added to timeline')),
                ('timeline_start_date', models.DateField(verbose_name='start date')),
                ('timeline_end_date', models.DateField(null=True, verbose_name='end date')),
                ('org_type', models.CharField(max_length=20)),
                ('org_name', models.CharField(max_length=50)),
                ('role_name', models.CharField(max_length=50)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Timeline_Event_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000, null=True)),
                ('degree', models.CharField(max_length=20, null=True)),
                ('timeline_event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume_builder.timeline_event')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
