# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from novel.models import novel_info
from novel.models import chapter_info


# 小说首页
def index(request):
    novelcopy = list(novel_info.objects)[:14]
    context = {
        'novels': novelcopy[:7],
        'novels2': novelcopy[7:],
    }
    return render(request, 'index.html', context=context)


# 单本小说列表页面
def book_info(request, novelid):
    novelcopy = novel_info.objects.filter(novelid=novelid)
    chaptercopy = chapter_info.objects.filter(novelid=novelid).order_by('order_id')
    context = {
        'novels': novelcopy,
        'chapters': chaptercopy,
    }
    return render(request, 'book_info.html', context=context)


# 小说章节内容页面
def chapter(request, novelid, chapterid):
    novelcopy = novel_info.objects.filter(novelid=novelid)
    chaptercopy = chapter_info.objects.filter(novelid=novelid, order_id=chapterid)
    chaptercopy1 = chapter_info.objects.filter(novelid=novelid, order_id=int(chapterid) - 1)
    chaptercopy2 = chapter_info.objects.filter(novelid=novelid, order_id=int(chapterid) + 1)
    context = {
        'novels':novelcopy,
        'chapters': chaptercopy,
        'chapters1': chaptercopy1,
        'chapters2': chaptercopy2,
    }

    return render(request, 'chapter.html', context=context)


def search(request):
    novelcopy = novel_info.objects.filter(name=request.POST['searchkey'])
    context = {
        'novels': novelcopy,
    }
    return render(request, 'search.html', context=context)


def sort(request):
    novelcopy = novel_info.objects.filter().order_by('?')[:8]
    context = {
        'novels': novelcopy[:4],
        'novels2': novelcopy[4:],
    }
    return render(request, 'sort.html', context=context)
