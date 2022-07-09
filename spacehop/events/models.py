from django.db import models

# Create your models here.

class Event(models.Model):
	"""
	Concrete base upon which all other events are created
	"""
	notes = models.CharField(max_length=2048, null=True)

class TextBox(Event):
	"""
	Event in which a textbox is displayed along the bottom of the screen
	"""
	speaker = models.ForeignKey('characters.Character', on_delete=models.SET_NULL, null=True)
	content = models.CharField(max_length=2048)

class FullscreenTextBox(Event):
	"""
	Event in which a textbox stretches across the entire screen, fading the background
	"""
	speaker = models.ForeignKey('characters.Character', on_delete=models.SET_NULL, null=True)
	content = models.CharField(max_length=4096)

class ChangeCharacters(Event):
	"""
	Event in which one or both of the characters are swapped out or removed
	"""
	character_one = models.ForeignKey('characters.Character', on_delete=models.SET_NULL, null=True, related_name="change_events_used_in_as_char_one")
	character_one_expression = models.ForeignKey('characters.Character', on_delete=models.SET_NULL, null=True, related_name="change_events_used_in_as_char_two")
	character_two = models.ForeignKey('characters.Character', on_delete=models.SET_NULL, null=True, related_name="change_events_used_in_as_char_expression_one")
	character_two_expression = models.ForeignKey('characters.Character', on_delete=models.SET_NULL, null=True, related_name="change_events_used_in_as_char_expression_two")

class ChangeAudio(Event):
	"""
	Event in which the background audio track is swapped or removed
	"""
	track = models.ForeignKey('sounds.AudioTrack', on_delete=models.SET_NULL, null=True)

class PlaySoundEffect(Event):
	"""
	Event in which a sound effect is played
	"""
	sound_effect = models.ForeignKey('sounds.SoundEffect', on_delete=models.SET_NULL, null=True)

class Delay(Event):
	"""
	Event in which nothing happens for a specified amount of time
	"""
	duration = models.DurationField()
