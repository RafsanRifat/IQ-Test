from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Questions, Question_sets, Options


# Create your views here.

def home(request):
    return render(request, 'home.html')


def iq_test(request):
    sets = Question_sets.objects.all()
    questions = Questions.objects.all()
    context = {'sets': sets, 'questions': questions}
    return render(request, 'test.html', context)


# def iq_api(request):
#     questions = Questions.objects.all()
#     return JsonResponse({"questions": list(questions.values())})

def options(request):
    options = Options.objects.all()
    context = {'options': options}
    return render(request, 'test.html', context)
