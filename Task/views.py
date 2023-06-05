from Task.forms import TaskRegistrationForm
from Task.models import SubTask,Task, User

# Create your views here.
# from django.shortcuts import redirect,render
# from Task.models import MyUser
from Task.serializers import LoginSerializer, SignUpSerializer
from rest_framework import generics, serializers
from rest_framework.response import Response
from .serializers import  SubTaskSerializer,TaskSerializer, SubTaskResSerializer
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


class TaskApiView(APIView):
    def get(self,request):
        if request.method =="GET":
            form = TaskRegistrationForm(request.GET)
            if form.is_valid():
                form.save
        task = Task.objects.all()
        serializer = TaskSerializer(task,many=True)
        return Response({"task":serializer.data})


class SubTaskApiView(generics.CreateAPIView):
    serializer_class = SubTaskSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        sub_task = SubTask.objects.create(
            assigned_by=serializer.validated_data.get('assigned_by'), 
            assigned_to=serializer.validated_data.get('assigned_to'), 
            task_id=serializer.validated_data.get('task_id'),
            task_name = serializer.validated_data.get('task_name'),
            description=serializer.validated_data.get('description'),
            creation_date=serializer.validated_data.get('creation_date'),
            due_date=serializer.validated_data.get('due_date'),
            completed=serializer.validated_data.get('completed')
            )
        return Response(data=SubTaskResSerializer(sub_task).data, status=201)
    

class SignUpApiView(generics.CreateAPIView):
    serializer_class = SignUpSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        task = authenticate(
            request,
            firstname = serializer.data['firstname'],
            lastname = serializer.data['lastname'],
            password = serializer.data['password'],
            confirm_password = serializer.data['confirm_password']
        )
        if task is not None:
            refresh = RefreshToken.for_user(task)
            return Response(
                {"refresh":str(refresh),"access":str(refresh.access_token)}
            )
        else:
            return Response(
                {"Invalid Information"}
            )
        
        # user = authenticate(
        #     request,
        #     firstname = serializer.data['firstname'],
        #     lastname = serializer.data['lastname'],
        #     password = serializer.data['password'],
        #     confirm_password = serializer.data['confirm_password']
        # )
        # if user is not None:
        #     refresh = RefreshToken.for_user(user)
        #     return Response(
        #         {"refresh":str(refresh),"access":str(refresh.access_token)}
        #     )
        # else:
        #     return Response(
        #         {"Invalid Information"}
        #     )

       
           









    






















    # def post(self,request):
    #   subtask = SubTask.objects.get(pk=pkg_resources)
    #   SubTask.objects.filter("task_id"==3)
    #   if request.method == "POST":
    #     # curren_subtask = request.SubTask.subtask
    #     data = request.POST
    #     action = data.get("follow")
    #     if action == "follow":
            # curren_subtask.follows.add(subtask)
        # elif action == "unfollow":
            #  curren_subtask.follows.remove(subtask)
        # curren_subtask.save()
        # Model.objects.filter(field_name=some_param)
# class AddSubTaskApiView(generics.CreateAPIView):
#     subtasks = SubTask.objects.all()
#     serializer_class = AddSubTaskSerializer
    # def post(self,request):
    #     subtask = request.data.get('task')
    #     serializer = TaskSerializer(data=subtask)
    #     if serializer.is_valid(raise_exception=True):
    #         subtask_saved =serializer.save
    #         return Response({"success":"SubTask '{}' created successfully".format(subtask_saved)})
 # if request.method =="POST":
            # form = TaskRegistrationForm(request.POST)
            # if form.is_valid():
            #     form.save
# class DataApiview(APIView):
#     serializer_class = DataModelSerializer
#     def get (self,request):
#         if request.method =="GET":
#             form = DataModelSerializer(request.GET)
#             if form.is_valid():
#                 datamodel = DataModel.objects.all()
#                 serializer = DataModelSerializer(datamodel,many=True)
#                 return Response({"datamodel":serializer.data})
    




                             



     
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # task = authenticate(
        #     request,
        #     task_name = serializer.data['task_name'],
        #     description = serializer.data["description"],
        #     title = serializer.data["title"],
        #     assigned_to = serializer.data["assigned_to"],
        #     assigned_by = serializer.data["assigned_by"],
        #     creation_date = serializer.data["creation_date"],
        #     due_date = serializer.data["due_date"],
        #     completed = serializer.data["completed"]
        # )
        # if task is not None:
        #     refresh = RefreshToken.for_user(task)
        #     return Response(
        #         {"refresh":str(refresh),"access":str(refresh.access_token)}
        #     )
        # else:
        #     return Response(
        #         {"No Tasks Assigned"}
        #     ) 

# class TaskApiView(APIView):
#     def get(self,request):
#         subtask=SubTask.objects.all()
#         serializer = TaskSerializer(subtask,many=True)
#         return Response({"subtask":serializer.data})