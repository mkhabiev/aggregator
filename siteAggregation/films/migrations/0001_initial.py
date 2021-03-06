# Generated by Django 3.1.4 on 2020-12-21 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Film title')),
                ('description', models.TextField(verbose_name='Film description')),
                ('date_filmed', models.PositiveSmallIntegerField(verbose_name='Date filmed')),
                ('duration', models.PositiveSmallIntegerField(verbose_name='Film duration')),
                ('age_limit', models.PositiveSmallIntegerField(default=3, verbose_name='Age limit')),
                ('review', models.FloatField(verbose_name='Average rating')),
            ],
        ),
    ]
