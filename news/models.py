from django.db import models

# Create your models here.


class News(models.Model):
    headline=models.CharField(max_length=50)
    body=models.TextField()
    date=models.DateField()