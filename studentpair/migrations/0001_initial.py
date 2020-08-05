# Generated by Django 3.0.9 on 2020-08-05 08:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cohort', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentPair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='start date')),
                ('end_date', models.DateField(verbose_name='end date')),
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cohort.Cohort')),
                ('first_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_student', to=settings.AUTH_USER_MODEL)),
                ('second_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_student', to=settings.AUTH_USER_MODEL)),
                ('third_student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'pairing',
            },
        ),
    ]
