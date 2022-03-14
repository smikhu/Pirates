# Generated by Django 4.0.3 on 2022-03-11 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0002_remove_film_creator_film_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='user',
        ),
        migrations.AddField(
            model_name='film',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]