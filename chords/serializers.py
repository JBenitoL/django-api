from rest_framework import serializers

from .models import Chord


class ChordSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    notes = serializers.ListField(child=serializers.IntegerField())
    class Meta:
        model = Chord
        fields = ["name", "notes"]

    def to_representation(self, instance):
        return super().to_representation(instance)

    def get_name(self, obj):
        return obj.name
    def get_notes(self, obj):
        return self.notes