from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question, Answer
from .forms import searchform 


# Create your views here.
def questions(request):
    latest_questions = Question.objects.all()
    context = {'latest_questions': latest_questions, 'form': searchform}
    return render(request, 'questions.html', context)
    
    
def questiondetail(request, question_id):
    question = get_object_or_404(Question, pk=question_id )
    return render(request, 'questiondetail.html', {'question': question, 'form': searchform})