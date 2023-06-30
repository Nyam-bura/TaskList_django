from rest_framework import serializers
from .models import Task, SubTask,User

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class SignUpSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['username','phone_number','email','password','id_number','county','id_document_type','confirm_password']
                 
class SignUpResSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = '__all__'

class SubTaskSerializer(serializers.ModelSerializer):
    assigned_to_name=serializers.CharField(source='assigned_to.username',read_only=True)
    assigned_by_name = serializers.CharField(source='assigned_by.username',read_only=True)
    # assigned_to_name = SignUpSerializer(read_only=True)
    # assigned_by_name = SignUpSerializer(read_only=True)
    class Meta:
        model = SubTask
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    sub_task= SubTaskSerializer(many=True,read_only=True,source='data')
    assigned_to_name = serializers.CharField(source='assigned_to.username',read_only=True)
    assigned_by_name = serializers.CharField(source='assigned_by.username',read_only=True)

    class Meta:
        model = Task
        exclude = ['assigned_to','assigned_by']

    def create(self, validated_data):
        return Task.objects.create(**validated_data)        