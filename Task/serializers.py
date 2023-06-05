from rest_framework import serializers
import Task
from .models import SubTask

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class SignUpSerializer(serializers.Serializer):
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()

class TaskSerializer(serializers.Serializer):
    task_id = serializers.IntegerField()
    task_name = serializers.CharField()
    description = serializers.CharField()
    assigned_to = serializers.CharField()
    assigned_by = serializers.CharField()
    creation_date = serializers.CharField()
    due_date = serializers.CharField()
    completed = serializers.CharField()

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

class SubTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubTask
        fields = ('task_id', 'task_name', 'assigned_to', 'assigned_by', 'description', 'creation_date', 'due_date', 'completed',)

class SubTaskResSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubTask
        fields = '__all__'



    # def create(self, validated_data):
        # return SubTask.objects.create(**validated_data)

# class AddSubTaskSerializer(serializers.Serializer):
#     class Meta:
#         model = SubTask
#         fields = ("task_id","task_name","description","assigned_to","assigned_by","creation_date","due_date","completed")
#         depth = 1

    


        