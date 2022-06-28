from .naming import ChordsNames
from .models import Chord

note_chords = {
    ChordsNames.M : [0, 4, 7],
    ChordsNames.m : [0, 3, 7],
    ChordsNames.hdis : [0, 3, 6],
    ChordsNames.maj7 : [0, 4, 7, 11],
    ChordsNames.m7 : [0, 3, 7, 10],
    ChordsNames.dom : [0, 4, 7, 10],
}


def init_bbdd(note_chords=note_chords):
    for name, notes in note_chords.items():
        Chord.objects.get_or_create(name=name, notes=notes)

