from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('task/<int:pk>/',views.task_view, name='task_view'),
    path('task/<int:pk>/delete/',views.delete_task_view,name='delete_task_view'),
    path('task/<int:pk>/toggle_status/',views.status_toggle_view,name='status_toggle_view'),
]