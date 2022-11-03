from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(verbose_name="Name", max_length=50)