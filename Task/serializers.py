from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class SignUpSerializer(serializers.Serializer):
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()
    
    
    
   
    
    
    