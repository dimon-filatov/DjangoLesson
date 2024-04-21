from django.urls import path
from . import views

app_name = 'quality_control'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('bugs/', views.bug_list, name='bugs'),
    path('bugs/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
    path('features/', views.feature_list, name='features'),
    path('features/<int:feature_id>/', views.FeatureView.as_view(), name='feature_id_detail'),
    path('bugs/new/', views.create_bug_report, name='create_bug_report'),
    path('features/new/', views.create_features, name='create_feature'),
]
