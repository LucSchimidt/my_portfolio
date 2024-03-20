from django.db import models


TYPES = (
	(0, 'Work'),
	(1, 'Blog')
)

class Item(models.Model):
    title = models.CharField(max_length=100)
    type =  models.CharField(max_length=10, choices=TYPES, default=0)
    content = models.CharField(max_length=2000)



TECH_LEVELS = (
    (0, 'Learning'),
    (0, '+1 year'),
    (0, '+2 years'),
    (0, '+3 years')
)

class Tech(models.Model):
    title = models.CharField(max_length=100)
    type =  models.CharField(max_length=10, choices=TECH_LEVELS, default=0)
    description = models.CharField(max_length=1000)


class Resume(models.Model):
    resume = models.FileField(upload_to='resume/', max_length=100)