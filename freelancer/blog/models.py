from django.db import models

# Create your models here.
class Post(models.Model):
    id: models.IntegerField()
    title: models.CharField(max_length=200)
    content: models.CharField()
    author: models.CharField(default='Ankur', max_length=200)
    date: models.CharField(max_length=20)
