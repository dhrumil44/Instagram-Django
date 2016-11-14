from __future__ import unicode_literals
from django.contrib.auth.models import User 
from django.conf import settings
from django.db import models

# Create your models here.
# class User(models.Model):
# 	name = models.CharField(max_length=20)

# 	def __str__(self):
# 		return self.name

# 	def __unicode__(self):
# 		return self.name

class Picture(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
	image = models.FileField(null=True, blank=True)

	# @property 
	# def image_url( self ):  
	#     try:
	#         img = open( self.image.path, "rb") 
	#         data = img.read() 
	#         return "data:image/jpg;base64,%s" % img.encode('base64') 
	 
	#     except IOError:
	#         return self.image.url
        
	def __str__(self):
		return self.user

	def __unicode__(self):
		return unicode(self.user)

class Friend(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,related_name='user')
	friend = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='friend')

	def __str__(self):
		return self.user

	def __unicode__(self):
		return unicode(self.user)