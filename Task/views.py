# from Task.forms import TaskRegistrationForm
from Task.models import Task, User

# Create your views here.
from Task.serializers import LoginSerializer, SignUpSerializer, SignUpResSerializer
from rest_framework import generics, serializers
from rest_framework.response import Response
from .serializers import  SubTaskSerializer,TaskSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView


class LoginApiView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            request,
            username=serializer.data["username"],
            password=serializer.data["password"],
        )
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response(
                {"refresh": str(refresh), "access": str(refresh.access_token)}
            )
        else:
            return Response({"Invalid Username and Password"})


class TaskApiView(generics.GenericAPIView):
    serializer_class = TaskSerializer
    def get(self,request):
        task = Task.objects.all()
        serializer = TaskSerializer(task,many=True)
        return Response({"task":serializer.data})


class SubTaskApiView(generics.CreateAPIView):
    serializer_class = SubTaskSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data,status=201)

class SignUpApiView(generics.CreateAPIView):
    serializer_class = SignUpSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError(detail='Ensure password match with confirm password', code=400)
        if User.objects.filter(username=data.get('email')).exists():
            raise serializers.ValidationError(detail='Username is already taken', code=400)
        new_user = User.objects.create_user(
            id_number = data.get('id_number'),
            username = data.get('username'),
            email=data.get('email'),
            password = data.get('password'),
            county=data.get('county'),
            id_document_type=data.get('id_document_type'),
            phone_number=data.get('phone_number')
            )
        self.serializer_class = SignUpResSerializer
        serialized_res = self.serializer_class(new_user)
        return Response(data=serialized_res.data, status=201)
