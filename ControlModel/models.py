from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Test(models.Model):
	name=models.CharField(max_length=20)
class User(models.Model):
	filename=models.CharField(max_length=30)
	headfile=models.FileField(upload_to='./upload/')

	def __unicode__(self):
		return self.filename

class DB_Stock(models.Model):
	Combin=models.CharField(max_length=255)
	ID=models.CharField(max_length=255)
	Name=models.CharField(max_length=255)
	Volume=models.IntegerField()

	def __unicode__(self):
		return self.ID
