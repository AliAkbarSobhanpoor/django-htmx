from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('element1', views.element1, name='element1'),
    path('element2', views.element2, name='element2'),
]