from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('register/', views.registrationPage, name="register"),
    path('', views.home, name="home"),
    path('patients/', views.patientList, name="patient_list"),
    path('register-patient/', views.registerPatient, name="register_patient"),
    path('edit-patient/<str:pk>/', views.editPatient, name="edit-patient"),
    path('delete-patient/<str:pk>/', views.deletePatient, name="delete-patient"),
    path('ward_list/', views.wardList, name="ward_list"),
]