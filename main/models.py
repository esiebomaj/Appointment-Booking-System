from django.db import models
from users.models import CustomUser

# Create your models here.


class HospitalSection(models.Model):
    name = models.CharField(max_length=100)


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    speciality = models.CharField(max_length=200)
    is_available = models.BooleanField(default=True)


class Appointment(models.Model):
    # models appointment between a doctor and patient
    patient = models.ForeignKey(
        CustomUser, related_name='patients', on_delete=models.CASCADE)
    doctor = models.ForeignKey(
        Doctor, related_name='appointments', on_delete=models.CASCADE)
    date = models.DateTimeField()
    time_alloted = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    is_confirmed = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    is_disabled = models.BooleanField(default=False)
    hospital_section = models.ForeignKey(
        HospitalSection, related_name='hospital_sections', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created_at',)
        get_latest_by = 'created_at'
