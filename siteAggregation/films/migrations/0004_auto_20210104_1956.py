# Generated by Django 3.1.4 on 2021-01-04 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_comment_show'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='show',
        ),
        migrations.AddField(
            model_name='tvshow',
            name='duration',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Show duration'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tvshow',
            name='release',
            field=models.CharField(choices=[('continued', 'Continued'), ('closed', 'Closed'), ('finished', 'Finished'), ('coming', 'Coming'), ('paused', 'Paused')], max_length=40),
        ),
    ]