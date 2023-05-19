from django.shortcuts import render
# Create your views here.
# from django.shortcuts import redirect,render
# from Task.models import MyUser
from Task.serializers import LoginSerializer, SignUpSerializer
from rest_framework import generics
from rest_framework.response  import Response
from django.contrib.auth import authenticate  
from rest_framework_simplejwt.tokens import RefreshToken


class LoginApiView(generics.GenericAPIView):
	serializer_class = LoginSerializer
	def post(self, request):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user= authenticate(request, username=serializer.data["username"],password=serializer.data["password"])
		if user is not None:
			refresh = RefreshToken.for_user(user)
			return Response(
				{"refresh":str(refresh),
				"access": str(refresh.access_token)
     }
			)
		else:
			return Response(
				{"Invalid Username and Password"}
			)
		
		
class SignUpApiView(generics.GenericAPIView):
	serializer_class = SignUpSerializer
	def post(self,request):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user= authenticate(request,firstname=serializer.data["firstname"],lastname=serializer.data["lastname"],password=serializer.data["password"],confirm_password=serializer.data["confirm_password"])
		if user is not None:
			refresh = RefreshToken.for_user(user)
			return Response(
				{"refresh":str(refresh),"access":str(refresh.access_token)}
			)
		else:
			return Response(
				{"Invalid Details"}
			)