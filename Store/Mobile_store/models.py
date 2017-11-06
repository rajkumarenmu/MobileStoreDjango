from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Brand(models.Model):
	brand_name = models.CharField(max_length = 50,unique=True)
	country =  models.CharField(max_length = 50)

	def __unicode__(self):
		return self.brand_name

class Mobiles(models.Model):
	brand_id = models.ForeignKey(Brand)
	model_no = models.CharField(max_length=10)
	description = models.TextField(max_length = 100)
	price = models.FloatField(max_length = 10)
	weight = models.FloatField(max_length = 10)
	ram = models.FloatField(max_length = 10)
	internal_memory = models.FloatField(max_length = 10)
	front_camera = models.CharField(max_length=10)
	image = models.ImageField(upload_to = 'static/uploads')

