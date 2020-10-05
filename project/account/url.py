from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'), #run
    path('doctor-register/', views.doc_register, name='doctor_reg'), #run
    path('patient-register/', views.patient_register, name='patient_reg'), #run
    path('login/', views.login_user, name='login'), #run
    path('patient-profile/<int:pk>', views.patient_profile, name='patient_profile'), #run
    path('doctor-profile/<int:pk>', views.doctor_profile, name='doctor_profile'), #run
    path('profile/<int:pk>', views.profile, name='profile'), #run
    path('patient-dashboard/', views.patient_dashboard, name='patient_dashboard'), #run
    path('doctor-dashboard/', views.doctor_dashboard, name='doctor_dashboard'), #run
    path('doctor-dashboard/<int:pk>/<approve>', views.doctor_approve, name='doctor_approve'), #run

    path('create_record/<int:pk>', views.create_record, name='created_record'), #run
    path('view_record/<int:pk>', views.view_record, name='view_record'),
    path('update_doctor_profile/<int:pk>/', views.update_doctor_profile, name='update_doctor_profile'), #run
    path('update_patient_profile/<int:pk>/', views.update_patient_profile, name='update_patient_profile'), #run
    path('change-password/', views.change_password, name='change_password'), #run
    path('add-clinic/', views.add_clinic, name='add_clinic'),
    path('add_tags/', views.add_tags, name='add_tags'),
    path('logout/', views.logout_user, name='logout'), #run
    path('search-doctor/', views.search_doctor, name='search_doctor'), #run
    path('add-social/', views.add_social, name='add_social'),
    path('doctor-profile/<int:pk>/book', views.book_appointment, name='book_appointment'), #run

]
