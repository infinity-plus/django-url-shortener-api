# Generated by Django 3.2 on 2021-07-12 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='ShorternedURL',
            fields=[
                ('id',
                 models.BigAutoField(auto_created=True,
                                     primary_key=True,
                                     serialize=False,
                                     verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('long_url', models.URLField()),
                ('short_url',
                 models.CharField(blank=True, max_length=15, unique=True)),
                ('times_visited', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
