import os
import requests

from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.db.models import F
from django.utils import timezone
# from django.urls import reverse
from django.views import generic
from django.shortcuts import render


# Create your views here.
def index(request):
    url = 'http://httpbin.org/get'
    r = requests.get(url)
    blizz = os.getenv('BLIZZARD_WEB_API_URL')
    return HttpResponse(blizz)

