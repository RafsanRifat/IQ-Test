from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .models import Questions, Question_sets, Options, Answer
# Program to generate a random number between 0 and 9

# importing the random module
import random


# Create your views here.

def home(request):
    return render(request, 'home.html')


def iq_test(request, total_correct_answer=None):
    sets = Question_sets.objects.all()
    set_item = []
    for set in sets:
        set_item.append(set.id)
    random_index = random.randint(0, len(set_item) - 1)
    print("This is random index", random_index)
    RandomQuestionSet = Question_sets.objects.filter(id=set_item[random_index]).first()
    questions = RandomQuestionSet.questions_set.all()
    single_question = []
    for question in questions:
        single_question.append(question)

    if request.method == "POST":
        answers = Answer.objects.all()
        for answer in answers:
            answers.filter()
            answer_id = answer.correct_answer.id

        for key, value in request.POST.lists():
            print(key, value)
            if key.split('-')[-1] != 'csrfmiddlewaretoken':
                qu_id = key.split('-')[-1]
                get_answer = Answer.objects.filter(question_id=qu_id,
                                                   correct_answer__option__contains=value[0])
                total_correct_answer = get_answer.count()
                if total_correct_answer == None:
                    return redirect('/')
                else:
                    context = {'score': total_correct_answer}
                    return render(request, 'result.html', context)
    context = {'questions': single_question, 'total_correct_answer': total_correct_answer}
    return render(request, 'test.html', context)

# def result(request):
#     return render(request, 'result.html')
