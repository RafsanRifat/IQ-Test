from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Questions, Question_sets


# Create your views here.

def home(request):
    return render(request, 'home.html')


def iq_test(request):
    sets = Question_sets.objects.all()
    questions = Questions.objects.all()
    context = {'questions': questions, 'sets': sets}
    return render(request, 'test.html', context)


def iq_api(request):
    return JsonResponse({"ths": 'dsf'})