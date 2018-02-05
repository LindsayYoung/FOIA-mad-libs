from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Document, Redaction, Position

def index(request):
    doc_list = Document.objects.all()
    context = {'doc_list': doc_list,}
    return render(request, 'foia/index.html', context)

def document(request, doc_id):
    doc = Document.objects.filter(name=doc_id).get()
    # redactions = Redaction.objects.filter(document=doc.id)
    redactions = doc.redaction_set.all()
    positions = redactions.get().position_set.all()

    return render(request, 'foia/document.html',
        {'document': doc, 'redactions': redactions, 'positions': positions},
    )
