from django.shortcuts import render
from myadmin.forms import QuestionEditForm
from polls.models import Question

# myadmin/views.py

def main(request):
    questions = Question.objects.all()

    return  render(request, 'myadmin/index.html', {'questions': questions})

def edit(request, id):
    question = Question.objects.get(id=id)

    form = QuestionEditForm(instance=question)

    if request.method == 'POST':
       form = QuestionEditForm(request.POST, instance=question)
       if form.is_valid():
           form.save()

    return  render(request, 'myadmin/edit.html', {'form': form, 'question': question})

#def votes_views(request, id):
#    votes =

