# Generated by Django 4.0.8 on 2022-12-24 11:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organazation_name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=100)),
                ('employee_count', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_address', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=100)),
                ('passport', models.CharField(blank=True, max_length=9, null=True)),
                ('email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('jins', models.IntegerField(blank=True, choices=[(1, 'ERKAK'), (2, 'AYOL')], default=1, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
