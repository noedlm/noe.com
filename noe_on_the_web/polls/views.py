from django.http import HttpRequest


# Create your views here.
def index(request):
    return HttpRequest("Hello world! you're at the polls index.")
