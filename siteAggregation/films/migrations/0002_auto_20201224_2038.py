# Generated by Django 3.1.4 on 2020-12-24 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TVShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='shows/')),
                ('title', models.CharField(max_length=150, verbose_name='Show title')),
                ('description', models.TextField(verbose_name='Show description')),
                ('date_showed', models.PositiveSmallIntegerField(verbose_name='Date showed')),
                ('release', models.CharField(choices=[('continued', 'Continued'), ('closed', 'Closed'), ('finished', 'Finished'), ('coming', 'Coming')], max_length=40)),
                ('age_limit', models.PositiveSmallIntegerField(default=3, verbose_name='Age limit')),
                ('review', models.FloatField(verbose_name='Average rating')),
                ('sound', models.CharField(max_length=150, verbose_name='Voice acting show')),
                ('episodes', models.PositiveSmallIntegerField(verbose_name='Show episode')),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='image',
            field=models.ImageField(default='sdfg', upload_to='films/'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('data_added', models.DateTimeField(auto_now_add=True)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='films.film')),
            ],
        ),
    ]
