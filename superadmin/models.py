from django.db import models
from datetime import date
# Create your models here.
class DineInTables(models.Model):
    table_no=models.CharField(max_length=10,primary_key=True)
    is_available=models.BooleanField(default=True)
    capacity=models.IntegerField(default=1)

class Rooms(models.Model):
    room_no=models.CharField(max_length=5,primary_key=True)
    room_type=models.CharField(max_length=50)
    is_available=models.BooleanField(default=True)
    price=models.FloatField(default=1000.00)
    start_date=models.DateField(auto_now=False, auto_now_add=False)
    room_image=models.ImageField(upload_to="media", height_field=None, width_field=None, max_length=None,default='0.jpeg')
    class Meta:
        db_table="rooms"

class superadminlogin(models.Model):
    email=models.EmailField(max_length=30,primary_key=True)
    password=models.CharField(max_length=15)
    class Meta:
        db_table="admindata"