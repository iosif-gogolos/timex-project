from django.contrib.auth.models import AbstractUser
from django.db import models
import secrets
import string

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


class TempWorker(AbstractUser):
    STATION_CHOICES = [
        ('station1', 'Station 1'),
        ('station2', 'Station 2'),
        # Weitere Stationen
    ]

    agency_name = models.CharField(max_length=100)
    station = models.CharField(max_length=50, choices=STATION_CHOICES)
    project_leader = models.ForeignKey('ProjectLeader', null=True, on_delete=models.SET_NULL)

    def generate_secure_password(self):
        """
        Generiert ein sicheres 8-stelliges Passwort
        mit Buchstaben, Zahlen und 2 Sonderzeichen
        """
        letters = string.ascii_letters
        digits = string.digits
        special_chars = '!@#$%^&*'

        password = [
            secrets.choice(letters),
            secrets.choice(letters.upper()),
            secrets.choice(digits),
            secrets.choice(digits),
            secrets.choice(special_chars),
            secrets.choice(special_chars)
        ]

        # Restliche Zeichen zufällig
        remaining_chars = letters + digits + special_chars
        password.extend(secrets.choice(remaining_chars) for _ in range(2))

        # Mischen der Zeichen
        secrets.SystemRandom().shuffle(password)
        return ''.join(password)

    def save(self, *args, **kwargs):
        if not self.password:
            raw_password = self.generate_secure_password()
            self.set_password(raw_password)
            # Optional: E-Mail mit Passwort senden
        super().save(*args, **kwargs)