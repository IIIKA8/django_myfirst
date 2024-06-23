from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

def base(request):
    return render(request, 'base.html')


def article1(request):
    return render(request, 'article/article1_FrendlyThug52NGG.html')

def article2(request):
    return render(request, 'article/article2_Baskov.html')

def article3(request):
    return render(request, 'article/article3_interesting.html')

def article4(request):
    return render(request, 'article/article4_questions_and_answers.html')

def article5(request):
    return render(request, 'article/article_main.html')

