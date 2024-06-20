from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

def base(request):
    return render(request, 'base.html')


def article1(request):
    return render(request, 'article/article1_FrendlyThug52NGG.html')

def article2(request):
    return render(request, 'article/article2_UNKI.html')
