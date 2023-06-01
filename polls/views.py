# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from django.views import generic

from polls.models import Question, Choice


def index_test(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def index_test1(request):
    context = {'hello': 'Hello World!'}
    return render(request, 'hello.html', context)


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = "last_question_list"

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'detail.html'


class ResultView(generic.DetailView):
    model = Question
    template_name = 'results.html'


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    last_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template('index.html')
    # output = ','.join([q.question_text for q in last_question_list])
    context = {"last_question_list": last_question_list}
    return render(request, 'index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # return HttpResponse("You're looking at question %s." % question_id)
    return render(request, "detail.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    return render(request, 'results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "you didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    # return HttpResponse("You're voting on question %s." % question_id)

# def index(request):
#     context = {}
#     context['hello'] = 'Hello World!'
#     return render(request, 'hello.html', context)
