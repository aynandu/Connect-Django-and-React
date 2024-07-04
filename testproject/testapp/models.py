from django.db import models

# Create your models here.
class Mymodel(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=40)
    mob=models.IntegerField(blank=False)