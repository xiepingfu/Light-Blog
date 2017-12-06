from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from . import models

# Create your views here.

def index(request):
    articles = models.article.objects.order_by('article_id')[:5]
    context = {'articles':articles}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def study(request):
    return render(request, 'study.html')