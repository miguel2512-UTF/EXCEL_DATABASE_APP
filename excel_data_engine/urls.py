from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.sheet_home, name='sheet_home'),
    path('create/', views.create_sheet),
    path('update/', views.update_sheet),
    path('get/<int:id>', views.get_sheet),
    path('refresh/<int:id_sheet>', views.refresh_sheet),
    path('api/<str:name>:<str:api_password>/data/<int:id_sheet>', views.get_sheet_data),
    path('api/activate/', views.active_api)
]    
