from django.contrib import admin

from .models import Document, Redaction, Position


class DocumentAdmin(admin.ModelAdmin):
    model = Document
    list_display = ['name', 'description']

admin.site.register(Document, DocumentAdmin)
admin.site.register(Redaction)
admin.site.register(Position)
