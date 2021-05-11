from django.db import models
from django.utils.timezone import now
# Create your models here.
class registrationmodel(models.Model):
    firstname=models.CharField(max_length=30,blank=False,default="tanuj")
    lastname=models.CharField(max_length=30,blank=False,default="tanuj")
    email=models.EmailField(primary_key=True,blank=False,max_length=100)
    password=models.CharField(max_length=20,blank=False)
    mobile=models.CharField(max_length=15,blank=False)
    address1=models.CharField(max_length=40,blank=False)
    address2=models.CharField(max_length=40,blank=False)
    city=models.CharField(max_length=30,blank=False)
    state=models.CharField(max_length=30,blank=False)
    zipcode=models.CharField(max_length=10,blank=False)
    class Meta:
        db_table="usersdata"

class bookroommodel(models.Model):
    email=models.CharField(max_length=40,blank=False,default="x")
    room_no=models.CharField(max_length=5,primary_key=True)
    room_type=models.CharField(max_length=50)
    price=models.FloatField(default=1000.00)
    start_date=models.DateField(auto_now=False, auto_now_add=False)
    end_date=models.DateField(auto_now=False, auto_now_add=False,default=now)
    class Meta:
        db_table="roombookings"