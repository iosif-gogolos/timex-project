from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('temp_worker', 'Zeitarbeitskraft'),
        ('project_leader', 'Projektleiter')
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    agency_name = models.CharField(max_length=120, blank=True, null=True)
    station = models.CharField(max_length=100, blank=True, null=True)

    def generate_username(selfself):
        return f"{self.first_name.lower()}.{self.last_name.lower()}"

class Workday(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    break_duration = models.IntegerField(default=0)
    total_work_hours = models.FloatField(default=0)
    worker_comment = models.TextField(blank=True, null=True)
    leader_comment = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, default='pending')