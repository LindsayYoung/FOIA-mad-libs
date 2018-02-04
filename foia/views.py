from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Document, Redaction, Position

def index(request):
    doc_list = Document.objects.all()
    context = {'doc_list': doc_list,}
    return render(request, 'foia/index.html', context)

def document(request, doc_id):
    doc = get_object_or_404(Document, name=doc_id)
    return render(request, 'foia/document.html', {'document': doc})
