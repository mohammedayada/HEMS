from django.shortcuts import render, redirect, HttpResponse, reverse
from . import models as m
from django.contrib.auth.models import User
from django.contrib import  messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import F, Q
# Create your views here.


def index(request):
    return render(request, 'account/index.html', {})


def about(request):
    return render(request, 'account/about.html')


def doc_register(request):

    List = ('Dentistry',
    'Oncology',
    'Ophthalmology',
    'Surgery medicine',
    'Hematology',
    'Mental Health Medicine',
    'Dermatology and Venereology',
    'Obstetrics and Gynecology',
    'Pediatrics')
    if request.method == "POST":
        cd = request.POST
        doctor = m.Doctor()
        doctor.user = User(username=cd['name'])
        doctor.age = cd['age']
        doctor.user.set_password(cd['password'])
        doctor.user.email = cd.get('email')
        doctor.phone = cd['phone_number']
        doctor.address, doctor.price, doctor.doctor_name = cd.get('address'), cd['price'], cd['name']
        doctor.gender, doctor.doctor_specialization, doctor.National_ID = cd.get('gender'), cd.get('doctor_specialization'), cd['id']
        doctor.user.save()
        doctor.save()
        messages.success(request, 'the account added successfully')
        return redirect('index')



    return render(request, 'account/doctor-register.html', {'List': List})


def patient_register(request):
    List = ('Dentistry',
    'Oncology',
    'Ophthalmology',
    'Surgery medicine',
    'Hematology',
    'Mental Health Medicine',
    'Dermatology and Venereology',
    'Obstetrics and Gynecology',
    'Pediatrics')
    if request.method == "POST":
        cd = request.POST
        patient = m.Patient()
        patient.user = User(username=cd['name'])
        patient.age = cd['age']
        patient.user.set_password(cd['password'])
        patient.user.email = cd.get('email')
        patient.phone = cd['phone_number']
        patient.address, patient.patient_birthday, patient.patient_name = cd.get('address'), cd['birthday'], cd['name']
        patient.gender, patient.doctor_specialization, patient.National_ID = cd.get('gender'), cd.get('doctor_specialization'), cd['id']
        patient.user.save()
        patient.save()
        messages.success(request, 'the account added successfully')
        return redirect('index')

    return render(request, 'account/register.html', {'List': List})



def login_user(request):
    if request.method == "POST":
        cd = request.POST
        user = authenticate(request, username=cd['username'], password=cd['password'])
        if user:
            login(request, user)

            if m.Doctor.objects.filter(user=user):
                return redirect('doctor_dashboard')
            if m.Patient.objects.filter(user=user):
                return redirect('patient_dashboard')

        else:
            messages.warning(request, 'something is went wrong check your info')
            return redirect('login')
    return render(request, 'account/login.html')
def profile(request,pk):
    try:
        doctor = m.Doctor.objects.get(pk=pk)
        if(doctor.user != request.user):
            return redirect('index')
        return render(request, 'account/doctor-profile.html', {'doctor': doctor})
    except:
        patient = m.Patient.objects.get(pk=pk)
        if (patient.user != request.user):
            return redirect('index')
        appointment = m.Appointment.objects.filter(patient=patient)
        record = m.Record.objects.filter(patient=patient)
        return render(request, 'account/patient-profile.html', {'patient': patient, 'appointments': appointment, 'records': record})

def patient_profile(request, pk):
    patient = m.Patient.objects.get(pk=pk)
    appointment = m.Appointment.objects.filter(patient=patient)
    record = m.Record.objects.filter(patient=patient)
    return render(request, 'account/patient-profile.html', {'patient': patient, 'appointments': appointment, 'records': record})

def doctor_profile(request, pk):
    if request.method == "POST":
        try:
            cd = request.POST
            appointment = m.Appointment()
            appointment.appointment_date = cd['book-time']
            patient = m.Patient.objects.filter(user=request.user)[0]
            appointment.patient = patient
            doctor = m.Doctor.objects.filter(user=pk)[0]
            appointment.doctor = doctor
            appointment.save()
            messages.success(request, 'appointment requested')
            return redirect('doctor_profile', pk=pk)
        except:
            messages.warning(request, 'appointment not requested')
            return redirect('doctor_profile', pk=pk)

    doctor = m.Doctor.objects.get(pk=pk)
    return render(request, 'account/doctor-profile.html', {'doctor': doctor})

@login_required(login_url='login')
def patient_dashboard(request):
    try:
        patient = m.Patient.objects.get(user=request.user)
        appointment = m.Appointment.objects.filter(patient=patient)
        record = m.Record.objects.filter(patient=patient)
        return render(request, 'account/patient-dashboard.html', {'patient': patient, 'appointments': appointment, 'records': record})
    except:
        return redirect('index')

@login_required(login_url='login')
def doctor_dashboard(request):
    try:
        doctor = m.Doctor.objects.get(user=request.user)
        appointment = m.Appointment.objects.filter(doctor=doctor)
        return render(request, 'account/doctor-dashboard.html', {'doctor': doctor, 'appointments': appointment})
    except:
        return redirect('index')

@login_required(login_url='login')
def doctor_approve(request, pk, approve):
    doctor = m.Doctor.objects.get(user=request.user)
    appointment = m.Appointment.objects.get(doctor=doctor, pk=pk)
    if(approve=="t"):
        appointment.approve = True
        appointment.save()
        messages.success(request, 'this appointment is accepted ')
    elif(approve=="f"):
        appointment.approve = False
        appointment.delete()
        messages.success(request, 'this appointment is not accepted and deleted ')
    else:
        messages.warning(request, 'please try again to accept this appointment ')
    return redirect('doctor_dashboard')



@login_required(login_url='login')
def update_doctor_profile(request, pk):
    obj = m.Doctor.objects.get(pk=pk)
    if(request.user != obj.user):
        return redirect('index')
    if request.method == "POST":
        cd = request.POST
        obj.doctor_name = cd['first_name']+' '+cd['last_name']
        obj.img = request.FILES.get('img')
        obj.bio = cd['bio']
        obj.phone = cd['phone']
        obj.save()
        messages.success(request,'profile updated successfully')
        return redirect('doctor_dashboard')

    return render(request, 'account/doctor-setting.html', {'obj': obj})

@login_required(login_url='login')
def update_patient_profile(request, pk):
    obj = m.Patient.objects.get(pk=pk)
    if(request.user != obj.user):
        return redirect('index')
    if request.method == "POST":
        cd = request.POST
        obj.patient_name = cd['first_name']+' '+cd['last_name']
        obj.img = request.FILES.get('img')
        obj.phone = cd['phone']
        obj.blood_group = cd.get('blood')
        obj.patient_birthday = cd['birthday']
        obj.user.email = cd['email']
        obj.age = cd['age']
        obj.save()
        messages.success(request,'profile updated successfully')
        return redirect('patient_dashboard')

    return render(request, 'account/patient-setting.html', {'obj': obj})





@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/chnge-password.html', {
        'form': form
    })








@login_required(login_url='login')
def add_clinic(request):
    cd = request.POST
    doctor = m.Doctor.objects.get(user=request.user)
    if m.Clinic.objects.filter(clinic_name=cd['clinic_name'],doctor=doctor,clinic_phone=cd['phone'], clinic_address=cd['address']):
        messages.warning(request, 'clinic added before')
        return redirect('doctor_dashboard')

    clinic = m.Clinic(doctor=doctor,clinic_phone=cd['phone'], clinic_address=cd['address'])
    if request.FILES.get('clinic_img'):
        clinic.img = request.FILES.get('clinic_img')

    clinic.save()
    messages.success(request, 'clinic added successfully')
    return redirect('doctor_dashboard')


from django.core import serializers
def add_tags(request):
    if request.is_ajax:
        print(request.POST.get("arr"))
        doctor = m.Doctor.objects.get(National_ID=int(request.POST.get("National_ID")))
        print(request.POST.get("National_ID"))
        for str in request.POST['arr']:
            doctor.tags += str.replace(" ", "")
        doctor.save()

    return JsonResponse({"instance": doctor}, status=200)


def logout_user(request):
    logout(request)
    return redirect('login')

def search_doctor(request):
    if request.method == 'GET':  # this will be GET now
        try:
            doctor_name = request.GET.get('search')  # do some research what it does
            doctor_specialization1 = request.GET.get('specialization1')
            doctor_specialization2 = request.GET.get('specialization2')
            doctor_specialization3 = request.GET.get('specialization3')
            doctor_specialization4 = request.GET.get('specialization4')
            doctor_specialization5 = request.GET.get('specialization5')
            doctor_specialization6 = request.GET.get('specialization6')
            doctor_specialization7 = request.GET.get('specialization7')
            doctor_specialization8 = request.GET.get('specialization8')
            doctor_specialization9 = request.GET.get('specialization9')
            gender1 = request.GET.get('gender1')
            gender2 = request.GET.get('gender2')
            status = m.Doctor.objects.all()
            if doctor_name:
                status = status.filter(Q(doctor_name__icontains=doctor_name))
            if gender1 or gender2:
                status = status.filter(Q(gender__icontains=gender1 or gender2))
            if doctor_specialization1 or doctor_specialization2  or doctor_specialization3  or doctor_specialization4 or doctor_specialization5 or doctor_specialization6 or doctor_specialization7 or doctor_specialization8 or doctor_specialization9:
                status = status.filter(Q(doctor_specialization__icontains=doctor_specialization1 or
                                                                           doctor_specialization2 or
                                                                           doctor_specialization3 or
                                                                           doctor_specialization4 or
                                                                           doctor_specialization5 or
                                                                           doctor_specialization6 or
                                                                           doctor_specialization7 or
                                                                           doctor_specialization8 or
                                                                           doctor_specialization9))
            return render(request, 'account/search-doctor.html', {'doctors': status})
        except:
            status = m.Doctor.objects.all()
            return render(request, 'account/search-doctor.html', {'doctors': status})

    else:
        doctors = m.Doctor.objects.all()
        return render(request, 'account/search-doctor.html', {'doctors': doctors})

@login_required(login_url='login')
def book_appointment(request, pk):
    if request.method == "POST":
        try:
            cd = request.POST
            appointment = m.Appointment()
            appointment.appointment_date = cd['book-time']
            patient = m.Patient.objects.filter(user=request.user)
            appointment.patient = patient
            doctor = m.Doctor.objects.filter(user=pk)
            appointment.doctor = doctor
            appointment.save()
            print(1)
            messages.success(request, 'appointment requested')
            return redirect('doctor_profile', pk=pk)
        except:
            print(2)
            messages.warning(request, 'appointment not requested')
            return redirect('doctor_profile', pk=pk)


@login_required(login_url='login')
def create_record(request, pk):
    if request.method == 'POST':
        appointment = m.Appointment.objects.get(pk=pk)
        if (appointment.approve == False):
            messages.warning(request, 'this record not created')
            return redirect('index')
        cd = request.POST
        record = m.Record()
        record.patient = appointment.patient
        record.doctor = appointment.doctor
        record.notes = cd['notes']
        record.record_description = cd['description']
        record.treatment = cd['treatment']
        record.save()
        messages.success(request, 'record created successfully')
        return redirect('patient_profile', pk=appointment.patient.pk)
    return render(request, 'account/create_record.html')

@login_required(login_url='login')
def view_record(request, pk):
    record = m.Record.objects.get(pk=pk)
    return render(request, 'account/create_record.html', {'record': record})

@login_required(login_url='login')  
def add_social(request):
    doc = m.Doctor.objects.get(user=request.user)

    if request.method == "POST":
        cd = request.POST
        doc.twitter = cd['twitter']
        doc.facebook= cd['facebook']
        doc.linkedin = cd['linkedin']
        doc.youtube = cd['youtube']
        doc.instagram = cd['instagram']
        doc.save()
        messages.success(request,'social info added successfully')
        return redirect('doctor_dashboard')

    return render(request, 'account/doctor-social.html', {'doc': doc})
