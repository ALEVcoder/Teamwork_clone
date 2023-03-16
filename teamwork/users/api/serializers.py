from django.contrib.auth import get_user_model
from rest_framework import serializers

from teamwork.users.models import Employee, Employer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "image", 'type', 'phone']

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "image", 'type', 'phone']

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["name", "image", 'type', 'phone']
    
class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "image", 'type', 'phone']

class UserTSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["name", "image"]

class EmployeeSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True, many=False)
    class Meta:
        model = Employee 
        fields = '__all__'

class TaskListSerializer(serializers.ModelSerializer):
    user = UserTSerializer(read_only=True, many=False)
    class Meta:
        model = Employee
        fields = ['user']
    
class EmployerSerializer(serializers.ModelSerializer):
    user = UserTSerializer(read_only=True, many=False)
    class Meta:
        model = Employer
        fields = '__all__'

