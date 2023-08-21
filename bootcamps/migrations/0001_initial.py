# Generated by Django 4.2.4 on 2023-08-19 14:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BootcampFirst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('faculty', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('level', models.CharField(choices=[('Higher Certificate', 'Higher Certificate'), ('Diploma', 'Diploma'), ('Honors', 'Honors'), ('Undergrad', 'Undergrad'), ('Post Graduate', 'Post Graduate'), ('Others', 'Others')], default='Undergrad', max_length=50)),
                ('expectation', models.TextField(max_length=800)),
                ('application_status', models.BooleanField(choices=[('Selected', 'Selected'), ('Rejected', 'Rejected')])),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Bootcamp September 2023',
                'verbose_name_plural': 'Bootcamp September 2023',
                'ordering': ['-date_created'],
            },
        ),
    ]
