from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User model
class User(AbstractUser):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Teacher', 'Teacher'),
         
        
    ]
    username=models.CharField(max_length=100, unique=True)
    password=models.CharField(max_length=20)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

# Student model
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=1,choices=[('M','Male'),('F','Female')])
    address=models.TextField()
    guardian_name=models.CharField(max_length=100)
    guardian_phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username

# Teacher model
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    t_name=models.CharField(max_length=50)
    address=models.CharField(max_length=20)
    phone=models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.user.username 

# subject model
class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject_name

# Class model
class Classroom(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Attendance model
class Attendance(models.Model):
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    reason=models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.student.user.username} - {self.status} on {self.date}"
    
#grade model
class Grade(models.Model):
    GRADE_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('F', 'F'),
    ]
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES)

    def __str__(self):
        return f"{self.student.user.username} - {self.subject.subject_name} - {self.grade}"


