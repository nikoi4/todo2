from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.TasksList.as_view(), name='tasks-list'),
]
