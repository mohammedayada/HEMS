from django.contrib import admin
from . import models as m
admin.site.register([m.Patient, m.Doctor, m.Bill, m.Clinic, m.Staff, m.Comment, m.Admin, m.Appointment, m.Record, m.Report])
# Register your models here.
