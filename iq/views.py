from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .models import Questions, Question_sets, Options, Answer
# Program to generate a random number between 0 and 9

# importing the random module
import random


# Create your views here.

def home(request):
    return render(request, 'home.html')


def iq_test(request):
    sets = Question_sets.objects.all()
    set_item = []
    for set in sets:
        set_item.append(set.id)
    random_index = random.randint(0, len(set_item) - 1)
    print("This is random index", random_index)
    RandomQuestionSet = Question_sets.objects.filter(id=set_item[random_index]).first()
    questions = RandomQuestionSet.questions_set.all()
    if request.method == "POST":
        for key, value in request.POST.lists():
            print(key, value)
        return redirect('/')
    context = {'questions': questions}
    return render(request, 'test.html', context)
