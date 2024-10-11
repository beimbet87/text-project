from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('input/', views.text_input_view, name='text_input'),
    path('export/', views.export_to_excel, name='export_to_excel'),
    path('result/', views.result_view, name='result_view')
]