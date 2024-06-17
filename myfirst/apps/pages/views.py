from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404



def index(request):
    return render(request, 'index.html')

def get_article(request, article_name):
    return render(request, f'article_about_rapers/{article_name}.html')
