# Generated by Django 3.1 on 2020-08-21 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_published', models.CharField(max_length=100)),
                ('headline', models.CharField(max_length=100)),
                ('article', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='HealthQuestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('how_often', models.CharField(max_length=100)),
                ('what_times', models.CharField(max_length=100)),
                ('favourite_way', models.CharField(max_length=100)),
                ('supplement', models.CharField(max_length=100)),
                ('Where_you_hear', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
