from django.db import models

# Create your models here.
class Product(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=255)
    category=models.CharField(max_length=255, db_index=True)
    price=models.FloatField(db_index=True)
    stock=models.BigIntegerField()
    created_at=models.DateTimeField(db_index=True)