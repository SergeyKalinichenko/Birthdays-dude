from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
#from django.utils import timezone
from django.urls import reverse
from .forms import ChoiceForm

from .models import Question, Choice

# polls/views.py

def greeting(request):
    return render(request, 'polls/greeting.html')


def index_view(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list,}
    return HttpResponse(template.render(context, request))


def results_view(request, pk):
    template_name = 'polls/results.html'
    return render(request, template_name, {'question': get_object_or_404(Question, pk=pk)})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        if request.POST.get('choice'):
            selected_choice = get_object_or_404(Choice, question=question, pk=request.POST.get('choice'))
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        else:
            return render(request, 'polls/detail.html', {'question': question, 'error_message': "You didn't select a choice!",})
    return render(request, 'polls/detail.html', {'question': question})


def add_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    form = ChoiceForm()
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            choice_text = form.cleaned_data['choice_text']
            for q in Question.objects.all():
                choice = Choice(choice_text=choice_text, question=q)
                choice.save()
            return HttpResponseRedirect(reverse('polls:vote', args=(question.id,)))
    return render(request, 'polls/add_question.html', {'form': form})


def contact(request):
    return render(request, 'polls/contact.html')
