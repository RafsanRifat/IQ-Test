from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    return render(request, 'home.html')


def iq_test(request):
    return render(request, 'test.html')
