from django.db import models

# Create your models here.

class Film(models.Model):
    """
    Model for storing film with their cast
    """
    image = models.ImageField(upload_to='films/')
    title = models.CharField('Film title', max_length=150)
    description = models.TextField('Film description')
    date_filmed = models.PositiveSmallIntegerField('Date filmed')
    duration = models.PositiveSmallIntegerField('Film duration')
    age_limit = models.PositiveSmallIntegerField('Age limit', default=3)
    review = models.FloatField('Average rating')

    def __str__(self):
        return self.title

class TVShow(models.Model):
    """
    Model for storing tvShows with Cast
    """
    rel_choices = (
        ('continued', 'Continued'),
        ('closed', 'Closed'),
        ('finished', 'Finished'),
        ('coming', 'Coming'),
    )

    image = models.ImageField(upload_to='shows/')
    title = models.CharField('Show title', max_length=150)
    description = models.TextField('Show description')
    date_showed = models.PositiveSmallIntegerField('Date showed')
    release = models.CharField(choices=rel_choices, max_length=40)
    age_limit = models.PositiveSmallIntegerField('Age limit', default=3)
    review = models.FloatField('Average rating')
    sound = models.CharField('Voice acting show', max_length=150)
    episodes = models.PositiveSmallIntegerField('Show episode')

    def __str__(self):
        return self.title