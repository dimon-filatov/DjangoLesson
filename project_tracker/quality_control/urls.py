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
    path('bugs/<int:bug_id>/update/', views.update_bug, name='update_bug'),
    path('features/<int:feature_id>/update/', views.update_features, name='update_features'),
    path('bugs/<int:bug_id>/delete/', views.delete_bug, name='delete_bug'),
    path('features/<int:feature_id>/delete/', views.delete_features, name='delete_feature'),
    path('bugs/', views.BugsListView.as_view(), name='bugs'),
    path('features/', views.FeaturesListView.as_view(), name='features'),
    path('bugs/<int:bug_id>/update/', views.BugUpdateView.as_view(), name='update_bug'),
    path('features/<int:feature_id>/update/', views.FeatureUpdateView.as_view(), name='update_features'),
    path('bugs/<int:bug_id>/delete/', views.BugDeleteView.as_view(), name='delete_bug'),
    path('features/<int:feature_id>/delete/', views.FeatureDeleteView.as_view(), name='delete_feature'),
]
