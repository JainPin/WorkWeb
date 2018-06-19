from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:OneWeb_id>/',views.blog,name='blog'),
    path('Note/',views.bNote,name='Note'),
]