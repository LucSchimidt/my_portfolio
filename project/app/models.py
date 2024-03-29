from django.db import models
from django.utils import timezone


TYPES = (
	(0, 'Work'),
	(1, 'Blog')
)

class Item(models.Model):
    title = models.CharField(max_length=100)
    type =  models.IntegerField(choices=TYPES, default=0)
    content = models.TextField()
    created_at = models.DateField(default=timezone.now)



TECH_LEVELS = (
    (0, 'Learning'),
    (1, '+1 year'),
    (2, '+2 years'),
    (3, '+3 years')
)

class Tech(models.Model):
    title = models.CharField(max_length=100)
    type =  models.IntegerField(choices=TECH_LEVELS, default=0)
    image = models.ImageField(upload_to='techs/', default='default_image.jpg')


class Resume(models.Model):
    resume = models.FileField(upload_to='resume/', max_length=100)