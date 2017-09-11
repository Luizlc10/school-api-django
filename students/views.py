from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer
# from __future__ import unicode_literals

from django.shortcuts import render


class StudentList(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": 1}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "403 Forbidden"}, status=status.HTTP_409_CONFLICT)


class StudentView(APIView):
    def get(self, request, pk=None):
        id = self.request.query_params.get('id', None)
        student = Student.objects.filter(id=id)
        if not student:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = StudentSerializer(student)
            return Response(serializer.data, status=status.HTTP_200_OK)
