from rest_framework import serializers
from .models import Note, Moeda


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content']

class MoedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moeda
        fields = ['id', 'nome', 'preco']