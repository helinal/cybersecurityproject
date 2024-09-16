from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from .models import Question, Choice

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = UserCreationForm.Meta.model
        fields = ["username", "password1", "password2"]

class AddPollForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']

class AddChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']

QuestionMetaInlineFormset = inlineformset_factory(
    Question,
    Choice,
    form=AddChoiceForm,
    extra=3,
    can_delete=False
)
