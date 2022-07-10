"""
Tests for spacehop
"""
from django.test import TestCase
from spacehop.sounds.models import AudioTrack, SoundEffect

class AudioTrackTestCase(TestCase):
	"""
	Test AudioTrack model
	"""
	def setUp(self) -> None:
		AudioTrack.objects.create(name="Test AudioTrack")

	def test_audio_track_model(self) -> None:
		return