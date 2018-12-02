from django.urls import path

from . import views

urlpatterns = [
    path('all', views.get_all_tasks, name='tasks_all'),
    path('todo', views.get_todo_tasks, name='todo'),
    path('inprogress', views.get_inprogress_tasks, name='inprogress'),
    path('done', views.get_done_tasks, name='done'),
    path('create', views.create_task, name='create'),
    path('delete', views.delete_task, name='delete'),
    path('show', views.show_task, name='show'),
    path('update', views.update_task, name='update'),
]