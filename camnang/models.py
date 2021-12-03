from django.db import models
from enum import unique
from django.db.models.deletion import PROTECT

# Create your models here.
class Camnang(models.Model):
    camnang_id = models.CharField(max_length=10, primary_key=True, unique=True, null=False, default='')
    camnang_name = models.CharField(max_length=200, default='')
    location = models.CharField(max_length=100, default='')
    view = models.PositiveIntegerField(default=0)
    date = models.DateField()
    decription = models.CharField(max_length=200, default='')
    
    def __str__(self):
        return self.name  