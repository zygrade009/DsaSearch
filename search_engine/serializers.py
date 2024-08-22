# search_engine/serializers.py
from rest_framework import serializers
from .models import Document, Vocabulary, InvertedIndex, QuestionLink

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

class VocabularySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocabulary
        fields = '__all__'

class InvertedIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvertedIndex
        fields = '__all__'

class QuestionLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionLink
        fields = '__all__'
