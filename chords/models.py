from django.db import models
from django.contrib.postgres.fields import ArrayField
from .naming import NoteNamesSharp

# Create your models here.

class Chord(models.Model):
    name = models.CharField(unique=True, max_length=256)
    notes = ArrayField(ArrayField(models.IntegerField()))

    def get_chord_notes_by_root(self, root_name:str):
        root_note_list = NoteNamesSharp.get_values()
        root_index = root_note_list.index(root_name)
        chord_notes = []
        for note_index in self.notes:
            chord_note_index = (note_index + root_index)%len(root_note_list)
            chord_notes.append(root_note_list[chord_note_index])
        return chord_notes

    @staticmethod
    def parse_chord_name(chord_name:str):
        root_note_list = NoteNamesSharp.get_values()
        sort_root_note_list = sorted(root_note_list, key=len, reverse=True)
        for note in sort_root_note_list:
            if note in chord_name:
                root_note = note
                chord_name = chord_name.replace(note, "")
                break
        return root_note, chord_name
        




    @classmethod
    def get_chord_notes(cls, chord_name:str):
        root_note, chord_name = cls.parse_chord_name(chord_name)
        chord_instance = cls.objects.get(name= chord_name)
        chord_notes = chord_instance.get_chord_notes_by_root(root_note)
        return chord_notes







