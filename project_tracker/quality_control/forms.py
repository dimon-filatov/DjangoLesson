from django.forms import ModelForm
from .models import BugReport, FeatureRequest


class BugReportForm(ModelForm):
    class Meta:
        model = BugReport
        fields = ['title', 'description', 'status', 'priority', 'project']


class FeatureRequestForm(ModelForm):
    class Meta:
        model = FeatureRequest
        fields = ['title', 'description', 'status', 'priority', 'project']
