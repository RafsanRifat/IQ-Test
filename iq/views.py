from django.shortcuts import render, HttpResponse
from .models import Questions

# Create your views here.

def home(request):
    return render(request, 'home.html')


def iq_test(request):
    questions = Questions.objects.all()
    context = {'questions': questions}
    return render(request, 'test.html', context)
