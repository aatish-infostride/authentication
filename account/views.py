from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from account.serializers import UserRegistrationSerializer

# Create your views here.

class UserRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
        
            user = serializer.save()
            
            return Response({'msg':'Registration Successful'},
            status=status.HTTP_201_CREATED)
        else: 
            return Response({'serializer.errors, status=status. HTTP_400_BAD_REQUEST'})
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)