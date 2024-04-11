from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse


def index(request):
    bugs_page_url = reverse('quality_сontrol:bugs')
    features_page_url = reverse('quality_сontrol:features')
    html = f"<h1>Система контроля качества</h1><a href='{bugs_page_url}'>Список всех багов</a><br><a href='{features_page_url}'>Запросы на улучшение</a>"
    return HttpResponse(html)


def bug_list(request):
    return HttpResponse("<h1>Cписок отчетов об ошибках</h1>")


def bug_detail(request, bug_id):
    return HttpResponse(f"Детали бага {bug_id}")


def feature_list(request):
    return HttpResponse("<h1>Список запросов на улучшение</h1>")


def feature_id_detail(request, feature_id):
    return HttpResponse(f"Детали улучшения {feature_id}")
