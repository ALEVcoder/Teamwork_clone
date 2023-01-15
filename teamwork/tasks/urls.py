from django.urls import path
from teamwork.tasks.views import (TasksApiView)

app_name = "tasks"
urlpatterns = [
    path('', TasksApiView.as_view(), name='tasks'),
]

