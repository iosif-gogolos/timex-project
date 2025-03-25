from datetime import timezone

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Workday


@login_required
def track_workday(request):
    worker = request.user
    today = timezone.now().date()

    # Aktuellen oder neuen Arbeitstag laden
    workday, created = Workday.objects.get_or_create(
        worker=worker,
        date=today
    )

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'clock_in':
            workday.start_time = timezone.now()
        elif action == 'pause_start':
            workday.pause_start = timezone.now()
        elif action == 'pause_end':
            workday.pause_end = timezone.now()
        elif action == 'clock_out':
            workday.end_time = timezone.now()
            workday.calculate_work_hours()

        workday.save()
        return redirect('workday_detail')

    return render(request, 'track_workday.html', {'workday': workday})