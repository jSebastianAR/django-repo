from django.db import models

# Create your models here.
class Product(models.Model):

	name 		= models.CharField(null=False,primary_key=True,max_length=100) #Primary key as the product's name 
	price 		= models.FloatField(null=False) #product's price
	description = models.CharField(null=False,primary_key=True,max_length=300) #product's description
	stock 		= models.IntegerField(null=False) 