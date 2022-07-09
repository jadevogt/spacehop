from django.db import models

class Chapter(models.Model):
	"""
	Largest organizational unit for the story
	"""
	title = models.CharField(max_length=128)
	scenes = models.ManyToManyField('Scene', through='Page')

class Scene(models.Model):
	"""
	A discrete series of Events in a Chapter
	"""
	title = models.CharField(max_length=128)
	# Character displayed on the left
	character_one = models.ForeignKey('characters.Character', on_delete=models.SET_NULL, null=True, related_name="scenes_used_in_by_default_as_char_one")
	character_one_expression = models.ForeignKey('characters.Expression', on_delete=models.SET_NULL, null=True, related_name="scenes_used_in_by_default_as_char_expression_one")
	# Character displayed on the right
	character_two = models.ForeignKey('characters.Character', on_delete=models.SET_NULL, null=True, related_name="scenes_used_in_by_default_as_char_two")
	character_two_expression = models.ForeignKey('characters.Expression', on_delete=models.SET_NULL, null=True, related_name="scenes_used_in_by_default_as_char_expression_two")
	events = models.ManyToManyField('events.Event', through='Sequence')

class Page(models.Model):
	"""
	Represents the relationship between a Scene and a parent Chapter
	"""
	chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
	scene = models.ForeignKey(Scene, on_delete=models.CASCADE)
	index = models.IntegerField()

class Sequence(models.Model):
	"""
	Represents the relationship between an Event and a parent Scene
	"""
	scene = models.ForeignKey(Scene, on_delete=models.CASCADE)
	textbox = models.ForeignKey('events.Event', on_delete=models.CASCADE)
	index = models.IntegerField()
