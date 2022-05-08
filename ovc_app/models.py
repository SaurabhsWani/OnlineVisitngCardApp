from django.db import models
from django.contrib.auth.models import AbstractUser
from matplotlib.pyplot import title
from .manager import UserManager

class User(AbstractUser):
    username=None
    email=models.EmailField(unique=True)
    mobile=models.CharField(max_length=14)
    address=models.CharField(max_length=200,null=True,blank=True)
    last_login_time=models.DateTimeField(null=True,blank=True)
    last_logout_time=models.DateTimeField(null=True,blank=True)
    objects=UserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

# class Card(models.Model):
#     cid=models.AutoField(primary_key=True)
#     style=models.CharField(max_length=100)
#     price=models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return str(self.cid)
class UserCardInformation(models.Model):
    uCardIfoId=models.AutoField(primary_key=True)
    cid=models.IntegerField()
    uid=models.IntegerField()
    heading=models.CharField(max_length=100)
    subheading=models.CharField(max_length=100)
    address=models.CharField(max_length=200,null=True,blank=True)
    website=models.CharField(max_length=100)
    mobile=models.CharField(max_length=14)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity=models.IntegerField()
    totalAmount=models.IntegerField()
    price_for_one=models.IntegerField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.uCardIfoId)

class OrderHistory(models.Model):
    oid=models.AutoField(primary_key=True)
    ucid=models.ForeignKey(UserCardInformation,related_name='orderhistory',on_delete=models.CASCADE)
    ordstatus=models.CharField(max_length=100, choices=[('pending','Pending'),('completed','Completed')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.oid)