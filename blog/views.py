from django.shortcuts import render
from django.http import HttpResponse

def post_list(request):
    return render(request, 'blog/post_list.html', {})

# Exemplos de como funciona os views. (Tudo aquilo que recebe um request e retorna um response)

def porta(request):
    return render(request, 'blog/porta.html', {})

def sala(request):
    return  HttpResponse("Você chegou a sala")
