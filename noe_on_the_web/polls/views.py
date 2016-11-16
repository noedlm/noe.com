from django.http import HttpResponse
from django.template import loader

from .models import Question


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    verb = "looking"
    return HttpResponse("You're %s at question %s" % (verb, question_id))


def results(request, question_id):
    response = "you're looking at the results of question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)


def test(request):
    return HttpResponse("returning the test view from the polls app!")


def not_found(request):
    return HttpResponse("Page not found!")
