"""foia_libs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import datetime

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from foia.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('doc/<str:doc_id>', views.document, name='document'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# need to test this
def handler404(request, error):
    now = datetime.datetime.now()
    response = render_to_response('404.html', {'errors': error, 'date-today': now.strftime("%B %d, %Y")},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response
