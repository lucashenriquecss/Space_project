from django.shortcuts import render,get_object_or_404
from .models import *
def index(request):
    posts = Gallery.objects.all()
    return render(request, 'gallery/index.html',{'posts':posts})


def imagem(request,id):
    detail = get_object_or_404(Gallery,pk=id)
    return render(request, 'gallery/imagem.html',{'detail':detail})
