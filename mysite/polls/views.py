from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .form import AddPollForm, QuestionMetaInlineFormset
from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def add(request):
    if request.method == 'POST':
        poll_form = AddPollForm(request.POST)
        formset = QuestionMetaInlineFormset(request.POST)
        
        if poll_form.is_valid() and formset.is_valid():
                    #Ensure at least two choices are filled
                    choices = formset.save(commit=False)
                    valid_choices = [choice for choice in choices if choice.choice_text.strip()]

                    if len(valid_choices) >= 2:
                        new_poll = poll_form.save(commit=False)
                        new_poll.save()

                        for choice in valid_choices:
                            choice.question = new_poll
                            choice.save()

                        return redirect('polls:index')
    else:
        poll_form = AddPollForm(initial={'pub_date': timezone.now()})
        formset = QuestionMetaInlineFormset()

    return render(request, 'polls/add.html', {
        'poll_form': poll_form,
        'formset': formset
    })