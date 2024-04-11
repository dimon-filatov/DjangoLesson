from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


def index(request):
    another_page_url = reverse('tasks:another_page')
    quality_control_page_url = reverse('quality_сontrol:index')
    html = f"<h1>Страница приложения Tasks</h1><a href='{another_page_url}'>Перейти на другую страницу</a><br><a href='{quality_control_page_url}'>Перейти на страницу багов и предложений</a>"
    return HttpResponse(html)


def another_page(request):
    return HttpResponse("Это другая страница приложения tasks.")
