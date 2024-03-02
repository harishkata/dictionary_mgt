from django.db import models

class Glass(models.Model):
    name = models.CharField(max_length=15)
    age = models.IntegerField()
    salary = models.IntegerField(null=True)