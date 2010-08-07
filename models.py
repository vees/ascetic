from django.db import models
from django.contrib.localflavor.us.models import PhoneNumberField

SALE_STATUS = ( 
	(1, "Held"), (2, "For Sale"), (3, "To Donate"), (4, "To Rent"),
	(5, "Sold"), (6, "Donated"), (7, "Lost"), (8, "Thrown Out")
)

class Picture(models.Model):
	photo = models.ImageField(upload_to='ascetic')
	caption = models.CharField(max_length=128, null=True, blank=True)
	def __unicode__(self):
		return self.caption

class Person(models.Model):
	first = models.CharField(max_length=128)
	last = models.CharField(max_length=128, null=True, blank=True)
	company = models.CharField(max_length=128, null=True, blank=True)
	email = models.EmailField(max_length=75, null=True, blank=True)
	phone = PhoneNumberField(unique=False, null=True, blank=True)
	notes = models.CharField(max_length=128, null=True, blank=True)
	def __unicode__(self):
		return self.last +', '+self.first

class Tag(models.Model):
	name = models.CharField(max_length=128)
	def __unicode__(self):
		return self.name

class Item(models.Model):
	nonce = models.CharField(max_length=8, null=True, blank=True)
	name = models.CharField(max_length=128)
	description = models.CharField(max_length=128, null=True, blank=True)
	purchase_cost = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
	purchase_date = models.DateField(null=True, blank=True)
	replacement_cost = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
	sale_price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
	owners = models.ManyToManyField(Person, null=True, blank=True)
	#http://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.ForeignKey
	parent = models.ForeignKey('self', null=True, blank=True) 
	related = models.ManyToManyField('self', null=True, blank=True)
	seperable = models.BooleanField(null=False)
	sale_status = models.IntegerField(choices=SALE_STATUS)
	pictures = models.ForeignKey(Picture, null=True, blank=True)
	tags = models.ManyToManyField(Tag, null=True, blank=True)
	description = models.CharField(max_length=1024, null=True, blank=True)
	upc = models.CharField(max_length=13, null=True, blank=True) # for EAN-13
	asin = models.CharField(max_length=10, null=True, blank=True)
	url = models.URLField(verify_exists=True, max_length=200, null=True, blank=True)
	last_edited = models.DateTimeField(auto_now=False, blank=True)
	def __unicode__(self):
		return self.name

class ConsumerItem(Item):
	manufacturer = models.CharField(max_length=128, null=True, blank=True)
	model = models.CharField(max_length=128, null=True, blank=True)
	serial = models.CharField(max_length=128, null=True, blank=True)

class MediaItem(Item):
	author = models.CharField(max_length=128, null=True, blank=True)
	title = models.CharField(max_length=128, null=True, blank=True)
	publisher = models.CharField(max_length=128, null=True, blank=True)
	isbn = models.CharField(max_length=13, null=True, blank=True)

class Group(models.Model):
	name = models.CharField(max_length=128)
	description = models.CharField(max_length=1024, null=True, blank=True)
	items = models.ManyToManyField(Item)
	def __unicode__(self):
		return self.name


