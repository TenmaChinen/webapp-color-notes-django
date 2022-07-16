# Generated by Django 3.2.6 on 2022-07-14 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notes', '0003_auto_20220714_1938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notemodel',
            name='user_name',
        ),
        migrations.AddField(
            model_name='notemodel',
            name='user_obj',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]