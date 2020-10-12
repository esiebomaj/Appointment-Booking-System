from django.db import models

# Create your models here.
class HospitalSection(models.Model):
    section_id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length = 100)

class Doctor(models.Model):
    doctor_id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length = 100)
    qualification = models.CharField(max_length = 100)
    speciality = models.CharField(max_length = 200)
    is_available = models.BooleanField(default=True)
    

class Appointments(models.Model):
    #models appointment between a doctor and patient
    appointment_id = models.UUIDField(primary_key=True, editable=False)
    patient_id = models.CharField(max_length=100)
    doctor_id = models.CharField(max_length=100)
    date =models.DateTimeField()
    time_alloted = models.DateTimeField()
    number_alloted = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    is_confirmed = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    is_disabled = models.BooleanField(default=False)
    section_id = models.CharField(max_length = 100)
    

    
    class Meta:
        ordering = ('created_at',)
        get_latest_by = 'created_at'
    