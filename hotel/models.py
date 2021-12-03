from enum import unique
from django.db import models
from django.db.models.deletion import PROTECT

# Create your models here.
class Img_slide(models.Model):
    img_id = models.CharField(max_length=10, primary_key=True, unique=True, null=False, default='')
    img = models.ImageField(max_length=100, default=None, upload_to='slide_hotel_img')
    hotel_id = models.ForeignKey('Hotel', on_delete=models.CASCADE, default='')
     
    def __str__(self):
        return self.img_id
    
class Firnish(models.Model):
     firnish_id = models.CharField(max_length=10, primary_key=True, unique=True, null=False, default='')
     firnish_name = models.CharField(max_length=100, default='') 
     hotel_id =models.ForeignKey('Hotel', on_delete=models.CASCADE, default='')
    
     def __str__(self):
         return self.firnish_name 
    
class Room(models.Model):
    room_id = models.CharField(max_length=10, primary_key=True, unique=True, null=False, default='')
    hotel_id = models.ForeignKey('Hotel', on_delete=models.CASCADE, default='')
    room_name = models.CharField(max_length=100, default='') 
    price = models.PositiveIntegerField(default='')
    valu = models.PositiveSmallIntegerField(default='')
    
    def __str__(self):
        return self.room_name
    
class Hotel(models.Model):
    hotel_id = models.CharField(max_length=10, primary_key=True, unique=True, null=False, default='')
    hotel_name = models.CharField(max_length=200, default='')
    location = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=100, default='')
    star = models.PositiveSmallIntegerField(default='')
    
    NEARBY_CHOICES = (
        ('B', 'Beach'),
        ('M', 'Mountain')
    )
    nearby = models.CharField(max_length=1, choices=NEARBY_CHOICES, default='B')
    map = models.URLField(max_length=200, default='')
    phone = models.IntegerField(default='')
    image = models.ImageField(max_length=100, default=None, upload_to='hotel_img')
    decription = models.TextField(default='')
    like = models.PositiveSmallIntegerField(default='')
    
    def __str__(self):
        return self.hotel_id
    