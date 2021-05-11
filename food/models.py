from django.db import models

# Create your models here.
class bookdineinmodel(models.Model):
    email=models.CharField(max_length=40,blank=False,default="x")
    table_no=models.CharField(max_length=10,blank=False)
    time=models.CharField(max_length=15,blank=False)
    space=models.CharField(max_length=10,blank=False,default="xc")
    class Meta:
        db_table="dineinbookings"
