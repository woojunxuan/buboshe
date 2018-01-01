# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from buboshe_app.models import Articles

# Create your views here.
def index(request):
    context = {}
    articles_list = Articles.objects.all().order_by('id')
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
