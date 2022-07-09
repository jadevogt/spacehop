from django.db import models

class AudioTrack(models.Model):
	"""
	Represent a background audio track
	"""
	name = models.CharField(max_length=128)

class SoundEffect(models.Model):
	"""
	Represent a sound effect
	"""
	name = models.CharField(max_length=128)