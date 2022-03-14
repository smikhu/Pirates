# Generated by Django 4.0.3 on 2022-03-12 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_favorite_img_favorite_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='favorites',
        ),
        migrations.AddField(
            model_name='favorite',
            name='film',
            field=models.ForeignKey(default=13, on_delete=django.db.models.deletion.CASCADE, to='main_app.film'),
            preserve_default=False,
        ),
    ]