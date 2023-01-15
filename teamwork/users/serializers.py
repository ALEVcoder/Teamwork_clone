from rest_framework import serializers
from django.contrib.auth import get_user_model

from teamwork.users.models import Employee, Employer 
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['name']

class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, many=True)
    class Meta:
        model = Employee 
        fields = '__all__'
    
class EmployerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, many=True)
    class Meta:
        model = Employer
        fields = '__all__'
