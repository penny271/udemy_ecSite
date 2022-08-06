from django.urls import path
from . import views

app_name= 'form_app'

url_patterns = [
    path('', views.index, name='index'),
    path('form_page', views.form_page),
]