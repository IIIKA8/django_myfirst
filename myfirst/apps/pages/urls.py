from django.urls import path
from . import views
from .views import get_article

urlpatterns = [
    path('', views.index, name='index'),
    path('get_article/<str:article_name>/', get_article, name='get_article'),
]
