# Create your views here.
from calendar import c
from urllib.parse import urlencode
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from chords.models import Chord
from rest_framework import mixins, status, viewsets
from chords.serializers import ChordSerializer


class ChordsViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet
):
    queryset = Chord.objects.all()
    serializer_class = ChordSerializer
    chord_name = "chord_name"



    @action(detail=False, methods=["post"])
    def get_chord_notes(self, request, **kwargs):
        chord_notes = Chord.get_chord_notes(self.request.data.get(self.chord_name))
        return Response(
            data=dict(status="ok", chord_notes = chord_notes),
            status=200,
        )