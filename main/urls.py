from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main_page'),
    path('cat_stats/', views.cat_stats, name='stats_page')
]