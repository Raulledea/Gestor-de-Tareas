from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('task/<int:pk>/',views.task_view, name='task_view'),
]