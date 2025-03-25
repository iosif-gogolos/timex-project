from django import forms
from .models import TempWorker

class TempWorkerCreationForm(forms.ModelForm):
    class Meta:
        model = TempWorker
        fields = [
            'first_name',
            'last_name',
            'email',
            'agency_name',
            'station',
            'project_leader'
        ]