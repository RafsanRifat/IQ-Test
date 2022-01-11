from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Questions, Question_sets, Options
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
    context = {'questions': questions}
    return render(request, 'test.html', context)

# def iq_api(request):
#     questions = Questions.objects.all()
#     return JsonResponse({"questions": list(questions.values())})

# def options(request):
#     if request.method =='GET':
#         options = Options.objects.get(id=id)
#     context = {'options': options}
#     return render(request, 'test.html', context)
