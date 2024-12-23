from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from django.http import JsonResponse
from .serializers import*
from rest_framework import viewsets
import json

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset=Subject.objects.all()
    serializer_class=SubjectSerializer

class ClassroomViewSet(viewsets.ModelViewSet):
    queryset=Classroom.objects.all()
    serializer_class=ClassroomSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset=Attendance.objects.all()
    serializer_class=AttendanceSerializer

class GradeViewSet(viewsets.ModelViewSet):
    queryset=Grade.objects.all()
    serializer_class=GradeSerializer
    

@api_view(['GET'])
def get_students(request, id=None):
    # if request.method=='GET':
    if id:
        student = Student.objects.all( id=id)
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# POST: Create a new student
@api_view(['POST'])
def post(request):
    # if request.method=='POST':
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def post(self, request, id):
        try:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
            # If the student does not exist, create a new one
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# PUT: Update an existing student by ID
@api_view(['PUT'])
def update(self, request, id):
        try:
            student = Student.objects.get(id=id)
            data = json.loads(request.body)

            student.name = data.get("name", student.name)
            student.age = data.get("age", student.age)
            student.grade = data.get("grade", student.grade)
            student.address = data.get("address", student.address)
            student.save()

            return JsonResponse({"message": "Student updated successfully"}, status=200)
        except Student.DoesNotExist:
            return JsonResponse({"error": "Student not found"}, status=404)

# DELETE: Delete an existing student by ID
@api_view(['DELETE'])
def delete(request, id=None):
    if not id:
        return Response({"error": "ID is required for deletion"}, status=status.HTTP_400_BAD_REQUEST)
    student = get_object_or_404(Student, id=id)
    student.delete()
    return Response({"message": "Student deleted successfully"}, status=status.HTTP_200_OK)


