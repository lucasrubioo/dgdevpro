from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {"posts": posts})







# Exemplos de como funciona os views. (Tudo aquilo que recebe um request e retorna um response)

# def porta(request):
#    return render(request, 'blog/porta.html', {})

# def sala(request):
#    return  HttpResponse("Você chegou a sala")
