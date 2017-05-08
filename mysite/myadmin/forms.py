from django.forms import ModelForm
from polls.models import Question, Choice


class QuestionEditForm(ModelForm):

    class Meta:
        model = Question
        fields = ('question_text',)

