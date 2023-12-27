from django.urls import path
from . import views


urlpatterns = [
    path('student_index/', views.student_index, name="student_index"),
    path('student_create/', views.student_create, name="student_create"),
    path('student_update/', views.student_update, name="student_update"),
    path('student_delete/', views.student_delete, name="student_delete"),
    path('health_index/', views.health_index, name="health_index"),
    path('health_risk/', views.health_risk, name="health_risk"),
]
