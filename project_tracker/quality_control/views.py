from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import BugReport, FeatureRequest


def index(request):
    bugs_page_url = reverse('quality_сontrol:bugs')
    features_page_url = reverse('quality_сontrol:features')
    html = f"<h1>Система контроля качества</h1><a href='{bugs_page_url}'>Список всех багов</a><br><a href='{features_page_url}'>Запросы на улучшение</a>"
    return HttpResponse(html)


def bug_list(request):
    bugs = BugReport.objects.all()
    bugs_html = "<h1>Cписок отчетов об ошибках</h1><ul>"
    for bug in bugs:
        bugs_html += f'<li><a href="{bug.id}/">{bug.title}</a> - {bug.status}</li>'
    bugs_html += '</ul>'
    return HttpResponse(bugs_html)


def bug_detail(request, bug_id):
    return HttpResponse(f"Детали бага {bug_id}")


def feature_list(request):
    features = FeatureRequest.objects.all()
    features_html = "<h1>Список запросов на улучшение</h1><ul>"
    for feature in features:
        features_html += f'<li><a href="{feature.id}/">{feature.title}</a> - {feature.status}</li>'
    features_html += '</ul>'
    return HttpResponse(features_html)


def feature_id_detail(request, feature_id):
    return HttpResponse(f"Детали улучшения {feature_id}")


from django.views import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        bugs_page_url = reverse('quality_сontrol:bugs')
        features_page_url = reverse('quality_сontrol:features')
        html = f"<h1>Система контроля качества</h1><a href='{bugs_page_url}'>Список всех багов</a><br><a href='{features_page_url}'>Запросы на улучшение</a>"
        return HttpResponse(html)


class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        bug = self.get_object()
        response_html = (f"<h1>{bug.title}</h1><p>{bug.description}</p><br>{bug.status} - {bug.priority}<br><br>"
                         f"<a href='/tasks/projects/{bug.project.id}/'>{bug.project.name}</a> / "
                         f"<a href='/tasks/projects/{bug.project.id}/tasks/{bug.task.id}/'>{bug.task.name}</a>")
        return HttpResponse(response_html)


class FeatureView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        feature = self.get_object()
        response_html = (
            f"<h1>{feature.title}</h1><p>{feature.description}</p><br>{feature.status} - {feature.priority}<br><br>"
            f"<a href='/tasks/projects/{feature.project.id}/'>{feature.project.name}</a> / "
            f"<a href='/tasks/projects/{feature.project.id}/tasks/{feature.task.id}/'>{feature.task.name}</a>")
        return HttpResponse(response_html)
