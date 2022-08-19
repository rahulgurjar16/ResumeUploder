from django.shortcuts import render
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class ProfileView(APIView):
    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Resume Uploded Successfully','status':'success','candidate':serializer.data},
            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)
    
    def get(self, request, format=None):
        candidates = Profile.objects.all()
        serializer = ProfileSerializer(candidates, many=True)
        return Response({'candidate':serializer.data},status=status.HTTP_201_CREATED)
        
