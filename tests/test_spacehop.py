from django.test import TestCase
from spacehop.characters.models import Character, Expression
from spacehop.events.models import Event, TextBox, FullscreenTextBox, ChangeCharacters, ChangeAudio, Delay
from spacehop.scenes.models import Scene, Sequence, Chapter, Page
from spacehop.sounds.models import AudioTrack, SoundEffect
from spacehop.images import *

class CharacterTestCase(TestCase):
	def setUp(self):
		Character.objects.create(name="Test Character")

class AnimalTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')