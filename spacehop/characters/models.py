from django.db import models

class Character(models.Model):
	"""
	Represent a character
	"""
	name = models.CharField(max_length=128)

class Expression(models.Model):
	"""
	Represent a specific expression of a character
	"""
	name = models.CharField(max_length=128)
	character = models.ForeignKey(Character, on_delete=models.CASCADE)