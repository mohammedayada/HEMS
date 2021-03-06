# Generated by Django 3.0.2 on 2020-08-07 01:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinic_name', models.CharField(default='', max_length=200, verbose_name='اسم العياده')),
                ('clinic_address', models.CharField(max_length=200, verbose_name='عنوان العياده')),
                ('clinic_phone', models.CharField(max_length=11, verbose_name='رقم الهاتف')),
                ('img', models.ImageField(null=True, upload_to='clinics')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('img', models.ImageField(null=True, upload_to='doctors')),
                ('bio', models.TextField(default='', max_length=5000, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('age', models.IntegerField(default=22)),
                ('doctor_name', models.CharField(max_length=120, verbose_name='اسم الدكتور')),
                ('doctor_specialization', models.CharField(choices=[('Dentistry', 'طب الأسنان'), ('Ophthalmology', 'طب العيون'), ('Oncology', 'طب الأورام'), ('Surgery medicine', 'طب الجراحة'), ('Hematology', 'طب أمراض الدم'), ('Mental Health Medicine', 'طب الصحة النفسية'), ('Dermatology and Venereology', 'طب الأمراض الجلدية والتناسلية'), ('Obstetrics and Gynecology', 'طب النساء والتوليد'), ('Pediatrics', 'طب الأطفال')], max_length=50, verbose_name='التخصص')),
                ('price', models.FloatField(default=0, verbose_name='سعر الكشف')),
                ('National_ID', models.CharField(max_length=14, unique=True, verbose_name='الرقم القومى')),
                ('phone', models.CharField(max_length=11, verbose_name='رقم الهاتف')),
                ('address', models.CharField(max_length=120, verbose_name='عنوان المستخدم')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, verbose_name='الجنس')),
                ('tags', models.TextField(default='', max_length=500, null='True')),
                ('youtube', models.CharField(default='', max_length=300)),
                ('facebook', models.CharField(default='', max_length=300)),
                ('twitter', models.CharField(default='', max_length=300)),
                ('instagram', models.CharField(default='', max_length=300)),
                ('linkedin', models.CharField(default='', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('img', models.ImageField(null=True, upload_to='patient')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('age', models.IntegerField(default=22)),
                ('patient_name', models.CharField(max_length=120, verbose_name='اسم المريض بالكامل')),
                ('patient_birthday', models.DateTimeField(verbose_name='تاريخ الميلاد')),
                ('National_ID', models.CharField(max_length=14, unique=True, verbose_name='الرقم القومى')),
                ('phone', models.CharField(max_length=11, verbose_name='رقم الهاتف')),
                ('address', models.CharField(max_length=120, verbose_name='عنوان المستخدم')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, verbose_name='الجنس')),
                ('doctor_specialization', models.CharField(choices=[('Dentistry', 'طب الأسنان'), ('Ophthalmology', 'طب العيون'), ('Oncology', 'طب الأورام'), ('Surgery medicine', 'طب الجراحة'), ('Hematology', 'طب أمراض الدم'), ('Mental Health Medicine', 'طب الصحة النفسية'), ('Dermatology and Venereology', 'طب الأمراض الجلدية والتناسلية'), ('Obstetrics and Gynecology', 'طب النساء والتوليد'), ('Pediatrics', 'طب الأطفال')], max_length=50, null=True, verbose_name='التخصص')),
                ('blood_group', models.CharField(default='A+', max_length=10)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('img', models.ImageField(null=True, upload_to='staff')),
                ('staff_birthday', models.DateTimeField(verbose_name='تاريخ الميلاد')),
                ('National_ID', models.CharField(max_length=14, primary_key=True, serialize=False, verbose_name='الرقم القومى')),
                ('phone', models.CharField(max_length=11, verbose_name='رقم الهاتف')),
                ('address', models.CharField(max_length=120, verbose_name='عنوان المستخدم')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, verbose_name='الجنس')),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Clinic')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Doctor')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_content', models.TextField(verbose_name='تقرير')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Staff')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_description', models.TextField(verbose_name='تقرير الحاله')),
                ('accessories', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Patient')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Staff')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=600, verbose_name=' اترك تعليقك')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Patient')),
            ],
        ),
        migrations.AddField(
            model_name='clinic',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Doctor'),
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='سعر التذكره')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateTimeField(auto_now_add=True)),
                ('appointment_update', models.DateTimeField(auto_now=True)),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Clinic')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Patient')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Staff')),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('img', models.ImageField(null=True, upload_to='admin')),
                ('admin_phone', models.CharField(max_length=11)),
                ('National_ID', models.CharField(max_length=14, primary_key=True, serialize=False, verbose_name='الرقم القومى')),
                ('phone', models.CharField(max_length=11, verbose_name='رقم الهاتف')),
                ('address', models.CharField(max_length=120, verbose_name='عنوان المستخدم')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, verbose_name='الجنس')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
