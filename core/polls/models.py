from django.db import models

class pollresult(models.Model):
    name = models.CharField(max_length = 101)
    age = models.CharField(max_length=101)
    district = models.CharField(max_length=101)
    choice = models.CharField(max_length=101)

