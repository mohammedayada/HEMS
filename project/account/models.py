from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.db.models import F
# Create your models here.
GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)
SPECIALIZATION_CHOICES = (
    ('Dentistry', 'طب الأسنان'),
    ('Ophthalmology', 'طب العيون'),
    ('Oncology', 'طب الأورام'),
    ('Surgery medicine', 'طب الجراحة'),
    ('Hematology', 'طب أمراض الدم'),
    ('Mental Health Medicine', 'طب الصحة النفسية'),
    ('Dermatology and Venereology', 'طب الأمراض الجلدية والتناسلية'),
    ('Obstetrics and Gynecology', 'طب النساء والتوليد'),
    ('Pediatrics', 'طب الأطفال')

)


class UserInfo(models.Model):
    National_ID = models.CharField(max_length=14, verbose_name='الرقم القومى', primary_key=True)
    phone = models.CharField(max_length=11, verbose_name='رقم الهاتف')
    address = models.CharField(max_length=120, verbose_name='عنوان المستخدم')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, verbose_name='الجنس')

    class Meta:
        abstract = True


class Doctor(models.Model):
    img = models.ImageField(upload_to='doctors', null=True)
    bio = models.TextField( default='',null=True, max_length=5000)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    age = models.IntegerField(default=22)
    doctor_name = models.CharField(max_length=120, verbose_name='اسم الدكتور')
    doctor_specialization = models.CharField(choices=SPECIALIZATION_CHOICES, max_length=50, verbose_name='التخصص')
    price = models.FloatField(verbose_name='سعر الكشف', default=0)
    National_ID = models.CharField(max_length=14, verbose_name='الرقم القومى',unique=True)
    phone = models.CharField(max_length=11, verbose_name='رقم الهاتف')
    address = models.CharField(max_length=120, verbose_name='عنوان المستخدم')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, verbose_name='الجنس')
    tags = models.TextField(max_length=500, null='True', default='')
    youtube = models.CharField(max_length=300, default='')
    facebook = models.CharField(max_length=300, default='')
    twitter = models.CharField(max_length=300, default='')
    instagram = models.CharField(max_length=300, default='')
    linkedin = models.CharField(max_length=300, default='')
    def __str__(self):
        return self.doctor_name




class Patient(models.Model):
    img = models.ImageField(upload_to='patient', null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    age = models.IntegerField(default=22)
    patient_name = models.CharField(max_length=120, verbose_name='اسم المريض بالكامل')
    patient_birthday = models.DateTimeField(verbose_name='تاريخ الميلاد')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    National_ID = models.CharField(max_length=14, verbose_name='الرقم القومى',unique=True)
    phone = models.CharField(max_length=11, verbose_name='رقم الهاتف')
    address = models.CharField(max_length=120, verbose_name='عنوان المستخدم')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, verbose_name='الجنس')
    doctor_specialization = models.CharField(choices=SPECIALIZATION_CHOICES, max_length=50, verbose_name='التخصص', null=True)
    blood_group = models.CharField(max_length=10, default='A+')
    def get_absolute_url(self):
        return reverse('account:profile', kwargs={
            'slug': self.id
        })
    def __str__(self):
        return self.patient_name





class Clinic(models.Model):
    clinic_name = models.CharField(default='',max_length=200,verbose_name='اسم العياده')
    clinic_address = models.CharField(max_length=200,verbose_name='عنوان العياده')
    clinic_phone = models.CharField(max_length=11,verbose_name='رقم الهاتف')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='clinics', null=True)





class Bill(models.Model):
    patient = models.OneToOneField(Patient,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5,decimal_places=2,verbose_name='سعر التذكره')
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    content = models.TextField(max_length=600,verbose_name=' اترك تعليقك')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Staff(models.Model):
    img = models.ImageField(upload_to='staff', null=True)
    staff_birthday = models.DateTimeField(verbose_name='تاريخ الميلاد')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic,on_delete=models.CASCADE)
    National_ID = models.CharField(max_length=14, verbose_name='الرقم القومى', primary_key=True)
    phone = models.CharField(max_length=11, verbose_name='رقم الهاتف')
    address = models.CharField(max_length=120, verbose_name='عنوان المستخدم')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, verbose_name='الجنس')



class Record(models.Model):
    record_description = models.TextField(verbose_name='تقرير الحاله')
    treatment = models.TextField(verbose_name='الأدويه', blank=True)
    notes = models.CharField(max_length=120, verbose_name='ملاحظات', blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return 'date: ' + str(self.created_at) + ' doctor: '+self.doctor.user.username + ' patient:'+self.patient.user.username


class Report(models.Model):
    report_content = models.TextField(verbose_name='تقرير')
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Appointment(models.Model):
    appointment_date = models.DateTimeField()
    appointment_update = models.DateTimeField(auto_now=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    approve = models. BooleanField(default=False)
    def __str__(self):
        return 'date: ' + str(self.appointment_date) + ' doctor: '+self.doctor.user.username + ' patient:'+self.patient.user.username

class Admin(models.Model):
    img = models.ImageField(upload_to='admin', null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    admin_phone = models.CharField(max_length=11)
    National_ID = models.CharField(max_length=14, verbose_name='الرقم القومى', primary_key=True)
    phone = models.CharField(max_length=11, verbose_name='رقم الهاتف')
    address = models.CharField(max_length=120, verbose_name='عنوان المستخدم')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, verbose_name='الجنس')

