"""
This file mocks out the tutor urls so that the spirit test can run
on travis-ci.org without having to download the main paneity django
project and it's tutor app
"""
from spirit.urls import *
from django.http import HttpResponse


def tutor(request):
    return HttpResponse("blah")


tutor_patterns = [
    url(r'^$', tutor, name='index'),
    url(r'^about/$', tutor, name='about'),
]


urlpatterns += [
    url(r'^tutor/', include(tutor_patterns, namespace='tutor', app_name='tutor')),
]
