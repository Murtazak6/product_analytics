from django.db import models

# Create your models here.
class Product(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=255)
    category=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10, decimal_places=3)
    stock=models.BigIntegerField()
    created_at=models.DateTimeField()