
from django.db import models

# from django.db.models import aggregates
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    Name=models.CharField(max_length=190,null=True)
    Email=models.CharField(max_length=190,null=True)
    phone=models.CharField(max_length=190,null=True)
    Age=models.CharField(max_length=190,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True) 
    advater=models.ImageField(blank=True,null=True,default="person1.jpg")

    def __str__(self):
        return self.Name

def __str__(self):
        return self.Name

class Tag(models.Model):
    Name=models.CharField(max_length=190,null=True)

    def __str__(self):
        return self.Name


class Book(models.Model):
    CATEGORY=(
        ('Classics','Classics'),
        ('Comic Book','Comic Book'),
        ('Fantasy', 'Fantasy'),
        ('Horror', 'Horror')
    )   

    name=models.CharField(max_length=190,null=True)
    author=models.CharField(max_length=190,null=True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=190,null=True,choices=CATEGORY)
    description=models.CharField(max_length=190,null=True)
    tags=models.ManyToManyField(Tag)
    date_created=models.DateTimeField(auto_now_add=True,null=True) 

    

class Order(models.Model):
    STATUS=(
        ('Pending','Pending'),
        ('Delievered','Delievered'),
        ('out of order', 'out of order'),
        ('in progress', 'in progress')
    )



    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    book=models.ForeignKey(Book,null=True,on_delete=models.SET_NULL)
    tags=models.ManyToManyField(Tag)
    

    date_created=models.DateTimeField(auto_now_add=True,null=True) 
    status=models.CharField(max_length=190,null=True,choices=STATUS)
       





      