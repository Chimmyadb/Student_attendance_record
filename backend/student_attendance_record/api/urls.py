
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from student_attendance.views import (
    get_students,
    post,
    update,
    delete,
)

urlpatterns = [
    
    path('students/', get_students, name='get_students'),  
    path('students/<int:id>/', get_students, name='get_student'),  
    path('students/create/', post, name='create_student'),
    path('students/update/', update, name='update_student'),  
    path('students/delete/<int:id>/', delete, name='delete_student'),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


