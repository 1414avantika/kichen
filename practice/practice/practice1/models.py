from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Register(models.Model):
    custmer_id=models.BigAutoField(max_length=200,primary_key=True)
    name=models.CharField(max_length=500)
    phone_no=models.IntegerField(null=True)
    email_id=models.EmailField()
    password=models.CharField(max_length=30)
    tiffin=models.IntegerField()
    start_date=models.DateField(auto_now_add=True)
    end_date=models.DateField()

class Main_Register(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=500)
    phone_no=models.IntegerField(null=True)
    email_id=models.EmailField()
    password=models.CharField(max_length=30)
    tiffin=models.IntegerField()
    start_date=models.DateField(auto_now_add=True)
    end_date=models.DateField()

    def __str__(self):
        return self.name



class yesno(models.Model):
    empl=models.ForeignKey(Main_Register,on_delete=models.CASCADE)
    Data = models.CharField(max_length=20,default=0)
    timestamp = models.DateTimeField(auto_now_add=True)




