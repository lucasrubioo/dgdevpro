from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list')

    
    #path('porta', views.porta), - Exemplos de como criar url para ser exibida pelo views
    #path('sala', views.sala)
]