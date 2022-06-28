from django.test import  TestCase
from rest_framework.test import APIClient, APIRequestFactory
from .utils import init_bbdd, note_chords
from .models import Chord
from .naming import ChordsNames
import json

# Create your tests here.
class ChordsTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        init_bbdd()
    def test_init_bbdd(self):
        
        self.assertEqual(Chord.objects.count(), len(note_chords))

    def test_chord_notes_by_root_CMaj7(self):
        chord_instance = Chord.objects.get(name=ChordsNames.maj7)

        self.assertEqual(chord_instance.get_chord_notes_by_root("C"), ["C", "E", "G", "B"])

    def test_chord_notes_by_root_Fm7(self):
        chord_instance = Chord.objects.get(name=ChordsNames.m7)
        self.assertEqual(chord_instance.get_chord_notes_by_root("F"), ["F", "G#", "C", "D#"])

    def test_get_chord_notes_Cmaj7(self):
        self.assertEqual(Chord.get_chord_notes("Cmaj7"), ["C", "E", "G", "B"])

    def test_get_chord_notes_Fm7(self):
        self.assertEqual(Chord.get_chord_notes("Fm7"), ["F", "G#", "C", "D#"])
    
    def test_get_chord_notes_Cmaj7(self):
        url = "/chords/get_chord_notes/"
        data= json.dumps(dict(chord_name="Cmaj7"))
        r = self.client.post(url, data, content_type="application/json",)
        self.assertEqual(r.json()["chord_notes"], ["C", "E", "G", "B"])
