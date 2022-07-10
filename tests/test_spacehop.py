"""
Tests for spacehop
"""
from django.test import TestCase
from spacehop.characters.models import Character, Expression
from spacehop.events.models import Event, TextBox, FullscreenTextBox, ChangeCharacters, ChangeAudio, Delay
from spacehop.scenes.models import Scene, Sequence, Chapter, Page
from spacehop.sounds.models import AudioTrack, SoundEffect
from spacehop.images import *

class CharacterTestCase(TestCase):
	"""
	Test Character models
	"""
	def setUp(self) -> None:
		Character.objects.create(name="Test Character")

	def run_some_other_test(self) -> None:
		return