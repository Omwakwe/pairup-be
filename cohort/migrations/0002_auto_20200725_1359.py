# Generated by Django 3.0.8 on 2020-07-25 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cohort', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cohort',
            options={'verbose_name_plural': 'cohort'},
        ),
        migrations.AddField(
            model_name='cohort',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
