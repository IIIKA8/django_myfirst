from django.urls import path
from . import views


urlpatterns = [
    path('', views.base, name='base'),
    path('article1_FrendlyThug52NGG', views.article1, name='article1'),
    path('article2_UNKI', views.article2, name='article2')
]
