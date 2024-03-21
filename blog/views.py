from django.shortcuts import render
from django.http import HttpResponse

# Exemplos de como funciona os views. (Tudo aquilo que recebe um request e retorna um response)
#def portao(request):
#    return HttpResponse("Você chegou ao portão da casa")

#def sala(request):
#    return  HttpResponse("Você chegou a sala")

def post_list(request):
    return render(request, 'blog/post_list.html', {})