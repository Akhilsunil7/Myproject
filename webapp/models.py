from django.db import models

# Create your models here.
class userdb(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    mobile=models.IntegerField(null=True,blank=True)
    password=models.CharField(max_length=25,null=True,blank=True)
    image=models.ImageField(upload_to="U_img",null=True,blank=True)


class cartdb(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    ProductName=models.CharField(max_length=100,null=True,blank=True)
    Description=models.CharField(max_length=100,null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    ProductImage=models.ImageField(upload_to="Product",null=True,blank=True)


