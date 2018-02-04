from django.db import models
from django.contrib import admin


class Document(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False)
    description = models.TextField()
    source = models.CharField(max_length=200)
    source_url = models.CharField(max_length=200)
    image = models.ImageField(unique=True, blank=False)

    def __str__(self):
        return self.name


class Redaction(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    redaction_id = models.CharField(max_length=200, unique=True, blank=False)
    foia_exemption = models.CharField(max_length=200)
    # def __init__(self):
    #     reaction_form_id = self.redaction_id.name + "-form

    def __str__(self):
        return self.redaction_id

class Position(models.Model):
    redaction = models.ForeignKey(Redaction, on_delete=models.CASCADE)
    px_top = models.IntegerField(blank=False)
    px_left = models.IntegerField(blank=False)
