from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .forms import TempWorkerCreationForm


@staff_member_required
def create_temp_worker(request):
    if request.method == 'POST':
        form = TempWorkerCreationForm(request.POST)
        if form.is_valid():
            worker = form.save()
            # Optional: Benachrichtigung senden
            return redirect('worker_list')
    else:
        form = TempWorkerCreationForm()

    return render(request, 'create_worker.html', {'form': form})