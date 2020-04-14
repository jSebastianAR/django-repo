from django.db import models


# Create your models here.
class Client(models.Model):
	id_client 	= models.AutoField(null=False,primary_key=True)
	name 		= models.CharField(max_length=30)
	last_name	= models.CharField(max_length=30)
	address		= models.CharField(max_length=100)	
	postal_code	= models.CharField(max_length=10)
	email		= models.CharField(max_length=50)		
	password	= models.CharField(max_length=10)