from django.urls import path
from . import views

app_name = 'algorithms'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('knapsack/', views.knapsack_view, name='knapsack'),
    path('scheduling/', views.scheduling_view, name='scheduling'),
]
