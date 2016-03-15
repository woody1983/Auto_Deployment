from django.shortcuts import render

# Create your views here.

def index(request):
    question_list = Question.objects.all()
    return render(
        request,
        "question/index.html",
        {'question_list': question_list},
    )
