from django.db import models
from django.utils import timezone

from users.models import TempWorker


class Workday(models.Model):
    worker = models.ForeignKey(TempWorker, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    pause_start = models.DateTimeField(null=True, blank=True)
    pause_end = models.DateTimeField(null=True, blank=True)
    total_work_hours = models.FloatField(default=0)
    status = models.CharField(max_length=20, default='pending')

    def calculate_work_hours(self):
        # Logik zur Berechnung der Arbeitszeit
        pass