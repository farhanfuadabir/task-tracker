from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:todo_id>/', views.details)
    # or
    # re_path(r'^details/(?P<todo_id>\w{0,50})/$', views.details)
]
