from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from teamwork.tasks.models import Tasks
from teamwork.tasks.serializers import TasksSerializer


class TasksApiView(ListAPIView):
    queryset = Tasks.objects.filter(is_active=True)
    serializer_class = TasksSerializer
    
    def get(self, request, *args, **kwargs):
        tasks = self.get_queryset()
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

