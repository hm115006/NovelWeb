# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from models import Noveltest
from models import Chaptertest

#小说首页
def index(request):
	novelcopy = Noveltest.objects.filter().order_by('?')[:14]
	context = {
		'novels': novelcopy[:7],
		'novels2': novelcopy[7:],
	}
	return render(request,'index.html',context=context)
#单本小说列表页面
def book_info(request,novelid):
	novelcopy = Noveltest.objects.filter(novelid=novelid)
	chaptercopy = Chaptertest.objects.filter(novelid=novelid)
	context = {
		'novels': novelcopy,
		'chapters': chaptercopy,
	}
	return render(request, 'book_info.html',context=context)
#小说章节内容页面
def chapter(request,chapterid):
	chaptercopy = Chaptertest.objects.filter(chapterid=chapterid)
	chaptercopy1 = Chaptertest.objects.filter(chapterid=int(chapterid) - 1)
	chaptercopy2 = Chaptertest.objects.filter(chapterid=int(chapterid) + 1)
	context = {
		'chapters': chaptercopy,
		'chapters1': chaptercopy1,
		'chapters2': chaptercopy2,
	}

	return render(request, 'chapter.html', context=context)
def search(request):
	novelcopy = Noveltest.objects.filter(novelname=request.POST['searchkey'])
	context={
		'novels':novelcopy,
	}
	return render(request,'search.html',context=context)

def sort(request):
	novelcopy = Noveltest.objects.filter().order_by('?')[:8]
	context = {
		'novels': novelcopy[:4],
		'novels2': novelcopy[4:],
	}
	return render(request,'sort.html',context=context)