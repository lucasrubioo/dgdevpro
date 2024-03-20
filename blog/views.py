from django.shortcuts import render
from django.http import HttpResponse

def portao(request):
    return HttpResponse("Você chegou ao portão da casa")

def sala(request):
    return  HttpResponse("Você chegou a sala")