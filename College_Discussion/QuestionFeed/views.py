from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question, Answer
from .forms import searchform, askquestionform, answerquestionform
from django.utils import timezone


# Create your views here.
def questions(request):
    if request.method == 'POST':
        questionform = askquestionform(request.POST)
        if questionform.is_valid():
            question = questionform.cleaned_data['question']
            tags = questionform.cleaned_data['tags']
            anonymous = questionform.cleaned_data['anonymous']
            if anonymous == True :
                questiondata = Question(question_text=question, user = "Anonymous", asked_date= timezone.now(), tags= tags)
                questiondata.save()
            else:
                questiondata = Question(question_text=question, user = "Saugat Sthapit", asked_date= timezone.now(), tags= tags)
                questiondata.save()
        else:
            return HTTPResponse("Wrong data.")
            
    latest_questions = Question.objects.all()
    context = {'latest_questions': latest_questions, 'form': searchform, 'askquestion': askquestionform }
    return render(request, 'questions.html', context)
    
    
def questiondetail(request, question_id):
    if request.method == 'POST':
        answerform = answerquestionform(request.POST)
        if answerform.is_valid():
            answer = answerform.cleaned_data['answer']
            answerdata = Answer(question= get_object_or_404(Question, pk=question_id ), answer_text= answer, user="Anonymous", answered_date=timezone.now())
            answerdata.save()
        else:
            return HTTPResponse("Wrong data")
        
    
    question = get_object_or_404(Question, pk=question_id )
    return render(request, 'questiondetail.html', {'question': question, 'form': searchform, 'answerquestion': answerquestionform })