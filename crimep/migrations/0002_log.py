# Generated by Django 3.2.9 on 2021-11-01 17:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crimep', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('location', models.CharField(max_length=50)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('num_reported', models.PositiveIntegerField()),
            ],
        ),
    ]