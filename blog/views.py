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
    check = models.article.objects.order_by('article_id')[5:10]
    next = str('')
    previous = str('disabled')
    if len(check) == 0:
        next = 'disabled'
    articles = models.article.objects.order_by('article_id')[:5]
    page = 1
    context = {'articles':articles,'previous':previous,'next':next,'nextpage':page+1,'prepage':page-1}
    return render(request, 'index.html', context)

def article(request,page):
    check = models.article.objects.order_by('article_id')[5*page:5*(page+1)]
    next = str('')
    previous = str('')
    if len(check) == 0:
        next = 'disabled'
    if page <= 1:
        previous = 'disabled'
    articles = models.article.objects.order_by('article_id')[5*(page-1):5*page]
    context = {'articles':articles,'previous':previous,'next':next,'nextpage':page+1,'prepage':page-1}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def study(request):
    return render(request, 'study.html')