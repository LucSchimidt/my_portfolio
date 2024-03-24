from django.db import models
from django.utils import timezone


TYPES = (
	(0, 'Work'),
	(1, 'Blog')
)

class Item(models.Model):
    title = models.CharField(max_length=100)
    type =  models.IntegerField(choices=TYPES, default=0)
    content = models.CharField(max_length=2000)
    created_at = models.DateField(default=timezone.now)



TECH_LEVELS = (
    (0, 'Learning'),
    (0, '+1 year'),
    (0, '+2 years'),
    (0, '+3 years')
)

class Tech(models.Model):
    title = models.CharField(max_length=100)
    type =  models.IntegerField(choices=TECH_LEVELS, default=0)


class Resume(models.Model):
    resume = models.FileField(upload_to='resume/', max_length=100)