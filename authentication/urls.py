from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.sign_in),
    path('logout/', views.terminate_session),
]