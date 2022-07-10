"""
Tests for spacehop
"""
from django.test import TestCase
from spacehop.characters.models import Character, Expression

class CharacterTestCase(TestCase):
	"""
	Test Character model
	"""
	def setUp(self) -> None:
		Character.objects.create(name="Test Character")

	def test_character_model(self) -> None:
		return