from django.db import models

class Cast(models.Model):
    """
    Model for staring cast of the films and shows
    """
    gender_choices = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other...')
    )

    image = models.ImageField(upload_to='cast/', null=True)
    name = models.CharField('Actor name', max_length=150)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(choices=gender_choices, max_length=40)
    films = models.ManyToManyField('films.Film', related_name='casts')

    def __str__(self):
        return self.title

class TVActor(models.Model):
    """
    Model for storing cast of the films and shows.
    """
    gender_choices = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other...')
    )
    name = models.CharField("Actor's name", max_length=150)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(choices=gender_choices, max_length=40)
    shows = models.ManyToManyField('films.TVShow')
    image = models.ImageField(upload_to='TVActor/', null=True)

    def __str__(self):
        return f'{self.name}'