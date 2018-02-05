from django.db import models
from django.contrib import admin


class Document(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False, help_text="Unique title that will appear in the page title. Don't give away exactly what it is.")
    description = models.TextField(help_text="Discribe the document, this will be in the alt text")
    source = models.CharField(max_length=200, help_text="The person or institution that requested or published the FOIA")
    source_url = models.CharField(max_length=200, help_text="Link to the source of the FOIA")
    image = models.ImageField(unique=True, blank=False, help_text="Upload FOIA image")
    text_color = models.CharField(max_length=200, help_text="Text color to match the redaction.")
    background_color = models.CharField(max_length=200, help_text="The color of the redaction. Generally, black or white.")
    font = models.CharField(max_length=200, help_text="The font that best matches the document")


class Redaction(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, help_text="The document this redaction belongs to")
    clue = models.CharField(max_length=200, unique=True, blank=False, help_text="The prompt that will help visitors guess what this redaction is.")
    redaction_id = models.CharField(max_length=200, unique=True, blank=False, help_text="name of this redaction")
    foia_exemption = models.CharField(max_length=200, help_text="For fun if you have it handy")

class Position(models.Model):
    redaction = models.ForeignKey(Redaction, on_delete=models.CASCADE)
    px_top = models.IntegerField(blank=False)
    px_left = models.IntegerField(blank=False)
