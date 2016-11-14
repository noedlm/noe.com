from django.http import HttpResponse


# Create your views here.
def index(request):
    a = "hello world"
    b = " from the new polls/index!"
    return HttpResponse(a + b)

def test(request):
    return HttpResponse("returning the test view from the polls app!")

def not_found(request):
    return HttpResponse("Page not found!")
