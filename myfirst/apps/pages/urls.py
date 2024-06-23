from django.urls import path
from . import views


urlpatterns = [
    path('', views.base, name='base'),
    path('article1_FrendlyThug52NGG', views.article1, name='article1'),
    path('article2_Baskov', views.article2, name='article2'),
    path('article3_interesting', views.article3, name='article3'),
    path('article4_questions_and_answers', views.article4, name='article4'),
    path('article_main', views.article5, name='article5')
]
