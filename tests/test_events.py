"""
Tests for spacehop
"""
from django.test import TestCase
from spacehop.events.models import Event, TextBox, FullscreenTextBox, ChangeCharacters, ChangeAudio, Delay

class EventTestCase(TestCase):
	"""
	Test Event model
	"""
	def setUp(self) -> None:
		Event.objects.create(notes="Test Event")

	def test_event_model(self) -> None:
		return