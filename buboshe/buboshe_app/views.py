# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from buboshe_app.models import Article, User
from django.contrib.auth import authenticate
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from buboshe_app.forms import RegisterForm

# Create your views here.
def index(request):
    context = {}
    articles_list = Article.objects.all().order_by('id')
    # 界面文章限定为9篇
    page_robot = Paginator(articles_list, 9)
    page_num = request.GET.get('page')
    try:
        articles_list = page_robot.page(page_num)
    except EmptyPage:
        articles_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        articles_list = page_robot.page(1)

    context['articles_list'] = articles_list
    return render(request, 'index.html', context)
    # return render(request, 'test.html', context)

def sign_in(request):
    return render(request, 'sign_in.html')


@csrf_exempt
def sign_up(request):
    """
    用户注册
    """
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm()
    return render(request, 'sign_up.html', context={'form': form})
