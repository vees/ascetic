from django.db import models

class Item(models.Model):
	#nonce
	#name
	#description
	#purchase_cost
	#purchase_date
	#replacement_cost
	#sale_price
	#owners
	#parent
	#seperable
	#sale_status
	#pictures
	#tags
	#description
	#upc
	#asin
	#urls
	#last_edited
	pass

class Group(models.Model):
	#items
	#description
	pass

class ConsumerItem(Item):
	#manufacturer
	#model
	#serial
	pass

class MediaItem(Item):
	#author
	#title
	#publisher
	#isbn
	pass

class Picture(models.Model):
	#filename
	pass

class Person(models.Model):
	#first
	#last
	#company
	#email
	#phone
	#notes
	pass

class Tag(models.Model):
	#name
	pass

class Status(models.Model):
	#name
	pass

