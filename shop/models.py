from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField #like primary key
    product_name=models.CharField(max_length=30)
    desc=models.CharField(max_length=200)
    published_date=models.DateField()
