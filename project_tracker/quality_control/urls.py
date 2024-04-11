from django.urls import path
from . import views

app_name = 'quality_сontrol'

urlpatterns = [
    path('', views.index, name='index'),
    path('bugs/', views.bug_list, name='bugs'),
    path('bugs/<int:bug_id>', views.bug_detail, name='bug_detail'),
    path('features/', views.feature_list, name='features'),
    path('features/<int:feature_id>', views.feature_id_detail, name='feature_id_detail'),
]
