from django.db import models

# Create your models here.
class Topic(models.Model):
    tname=models.CharField(max_length=100)
class Webpage(models.Model):
    tname=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()
class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=100)
