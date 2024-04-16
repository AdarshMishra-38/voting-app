from django.db import models

# Create your models here.

    
class queries(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    subject = models.CharField(max_length = 100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add= True)
