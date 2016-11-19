from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Question


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    context = {'results': "you're looking at the results of question %s" % question_id}
    return render(request, 'polls/results.html', context)


def vote(request, question_id):
    return render(request, 'polls/vote.html', {'vote': "these are the votes for question %s" % question_id})


def test(request):
    return HttpResponse("returning the test view from the polls app!")


def not_found(request):
    return HttpResponse("Page not found!")
