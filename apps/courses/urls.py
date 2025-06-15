from django.urls import path
from . import views
# from django.contrib import admin


urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('detail/', views.course_detail, name='course_detail'),
    path('lessons/', views.course_lesson, name='course_lesson'),
]