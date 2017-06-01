# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	"""docstring for User"models.Modelf __init__(self, arg):
		super(User,models.Model.__init__()
		self.arg = arg
	"""
	username=models.CharField(max_length=50)
	password=models.CharField(max_length=50)
	name=models.CharField(max_length=50)
	email=models.EmailField(max_length=50)

	def __str__(self):
		return self.name