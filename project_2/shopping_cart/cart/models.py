from django.db import models
from product.models import Product
from client.models import Client
# Create your models here.

class Cart():

	def __init__(self,id_client):

		self.list_products		= []
		self.product_quantity 	= {}
		self.id_client			= id_client
		self.total_price		= 0.0

	def get_totalPrice(self):

		total = 0.0
		for product in self.list_products:
			total += product.price

		self.total_price = total

	"""
	This function adds the chosen product by the client to the cart

	PARAMS:
	self = the client's cart
	nameProduct = The chosen product by the client to add to the cart
	quantity = How many pieces of the same product the client wants

	"""	
	def add_product(self,nameProduct,quantity):
		try:

			product = Product.objects.get(name=nameProduct) #This sentence could trigger the exception
			
			if product.stock==0 and product.stock<quantity: #Sold Out

				return "The product is not available"
			else:

				self.list_products.append(product)
				self.product_quantity[product.name] = quantity

		except E: 

			return "The product doesnt exist in the shop anymore, exception: "+E

	"""
	
	This function removes a specific product from the client's cart including all the pieces that were added

	PARAMS:
	self = the client's cart
	nameProduct = The name of the product that the client wants to remove from the cart

	"""		
	def remove_product(self,nameProduct):

		try:
			product = Product.objects.get(name=nameProduct) #This sentence could trigger the exception

			if product in self.list_products:
				self.list_products.remove(product) #removes the product from the list
				del self.product_quantity[product.name] #removes the product from the dict of quantities
				return "Product removed from cart"
			else:
				return "The product couldnt be deleted because doesnt exist in the cart"
		except E:
			return "The product doesnt exist in the shop anymore, exception: "+E		

	"""
	
	This function substract one piece from the product chosen, from the client's cart

	PARAMS:
	self = the client's cart
	nameProduct = The name of the product wich the client wants to substract one piece
	
	"""
	def substract_product(self,nameProduct):
		
		try:
			
			self.product_quantity[nameProduct] -= 1 

		except E:
			return "The product doesnt exist in the cart anymore, exception: "+E

	"""
	
	This function adds one piece from the product chosen, from the client's cart

	PARAMS:
	self = the client's cart
	nameProduct = The name of the product wich the client wants to add one piece
	
	"""		
	def add_new_piece(self,nameProduct):
		
		try:
			
			self.product_quantity[nameProduct] += 1 

		except E:
			return "The product doesnt exist in the cart anymore, exception: "+E	
