from django.db import models

# Create your models here.

class todomodel(models.Model):
    item=models.TextField(null=False)

