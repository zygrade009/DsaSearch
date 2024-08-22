# search_engine/models.py
from django.db import models

class Document(models.Model):
    content = models.TextField()

class Vocabulary(models.Model):
    term = models.CharField(max_length=255)
    idf_value = models.FloatField()

class InvertedIndex(models.Model):
    term = models.CharField(max_length=255)
    document_ids = models.JSONField()  # List of document IDs

class QuestionLink(models.Model):
    url = models.URLField()
    source = models.CharField(max_length=255)
