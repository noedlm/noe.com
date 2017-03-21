from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.db.models import F
from django.utils import timezone
# from django.urls import reverse
from django.views import generic
from django.shortcuts import render


# Create your views here.
def index(request):

    return HttpResponse('just a string here')

