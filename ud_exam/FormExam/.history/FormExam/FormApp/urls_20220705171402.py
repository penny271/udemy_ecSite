from django.urls import path
from . import views

#- app_name 重要!! {% url 'form_app:sample.html'などで仕様}

urlpatterns = [
    path('insert_student/', views.insert_student, name='insert_student'),
]