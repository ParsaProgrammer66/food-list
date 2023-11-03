from django.db import models

class Products(models.Model):

    def __str__(self):
        return self.title
    title=models.CharField(max_length=200)
    price=models.FloatField()
    discount_price=models.FloatField()
    category=models.CharField(max_length=200)
    discription=models.TextField()
    image=models.CharField(max_length=300)

class Ord(models.Model):
    Items=models.CharField(max_length=1000)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    address=models.CharField(max_length=1000)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    zipcode=models.CharField(max_length=200)
    total=models.CharField(max_length=200)

