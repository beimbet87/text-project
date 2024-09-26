from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('input/', views.text_input_view, name='text_input'),
]