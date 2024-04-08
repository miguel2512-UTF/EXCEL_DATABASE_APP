from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.excel_home, name='excel_home'),
    path('create/', views.create_excel),
    path('update/', views.update_excel),
    path('get/<int:id>', views.get_excel),
    path('refresh/<int:id_sheet>', views.refresh_excel),
    path('api/data/<int:id_sheet>    ', views.get_sheet_data),
    path('api/<str:name>/data/<int:id_sheet>', views.get_sheet_data)
]    
