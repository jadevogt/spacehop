"""
Tests for spacehop
"""
from django.test import TestCase
from spacehop.scenes.models import Scene, Sequence, Chapter, Page

class SceneTestCase(TestCase):
	"""
	Test Scene model
	"""
	def setUp(self) -> None:
		Scene.objects.create(title="Test Scene")

	def test_scene_model(self) -> None:
		return