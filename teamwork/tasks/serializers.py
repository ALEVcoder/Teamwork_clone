from rest_framework import serializers

from teamwork.tasks.models import Tasks
from teamwork.users.serializers import EmployerSerializer

class TasksSerializer(serializers.ModelSerializer):
    # employee = EmployeeSerializer(read_only=True, many=True)
    employer = EmployerSerializer(read_only=True, many=True)

    class Meta:
        model = Tasks 
        fields = ['id', 'employee', 'employer', 'specialty', 'title', 'amount', 'time', 'status', 'description']
