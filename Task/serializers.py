from rest_framework import serializers
from .models import Task, SubTask

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class SignUpSerializer(serializers.Serializer):
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()

class SubTaskSerializer(serializers.ModelSerializer):
    assigned_to_name=serializers.CharField(source='assigned_to.username',read_only=True)
    assigned_by_name = serializers.CharField(source='assigned_by.username',read_only=True)
    class Meta:
        model = SubTask
        exclude = ['assigned_to','assigned_by']


class TaskSerializer(serializers.ModelSerializer):
    sub_task= SubTaskSerializer(many=True,read_only=True,source='data')
    assigned_to_name = serializers.CharField(source='assigned_to.username',read_only=True)
    assigned_by_name = serializers.CharField(source='assigned_by.username',read_only=True)
    class Meta:
        model = Task
        exclude = ['assigned_to','assigned_by']

    def create(self, validated_data):
        return Task.objects.create(**validated_data)    



    # def create(self, validated_data):
        # return SubTask.objects.create(**validated_data)

# class AddSubTaskSerializer(serializers.Serializer):
#     class Meta:
#         model = SubTask
#         fields = ("task_id","task_name","description","assigned_to","assigned_by","creation_date","due_date","completed")
#         depth = 1

    


        