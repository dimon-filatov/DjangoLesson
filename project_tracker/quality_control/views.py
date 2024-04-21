from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import BugReport, FeatureRequest


# def index(request):
#     bugs_page_url = reverse('quality_сontrol:bugs')
#     features_page_url = reverse('quality_control:features')
#     html = f"<h1>Система контроля качества</h1><a href='{bugs_page_url}'>Список всех багов</a><br><a href='{features_page_url}'>Запросы на улучшение</a>"
#     return HttpResponse(html)


def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bugs_list.html', {'bugs_list': bugs})


def bug_detail(request, bug_id):
    return HttpResponse(f"Детали бага {bug_id}")


def feature_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_list.html', {'feature_list': features})


def feature_id_detail(request, feature_id):
    return HttpResponse(f"Детали улучшения {feature_id}")


from .forms import BugReportForm, FeatureRequestForm
from django.shortcuts import render, redirect


def create_bug_report(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bugs')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_report_create.html', {'form': form})


def create_features(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:features')
    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/feature_request_form.html', {'form': form})


from django.views import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')


class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_detail.html'
    context_object_name = 'bug'


class FeatureView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    template_name = 'quality_control/feature_detail.html'
    context_object_name = 'feature'
