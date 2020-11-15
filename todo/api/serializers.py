# Return model object in a json Response
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    # Use Meta class to encapsulate all fields of the models
    # Otherwise use serializer to define validation rules explicitly
    class Meta:
        model = Task
        fields = '__all__'
