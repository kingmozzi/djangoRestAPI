from django.db import models

# Create your models here.
class Practice(models.Model):
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
