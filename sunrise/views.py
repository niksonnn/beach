from django.shortcuts import render, get_object_or_404
from .models import Beach, Rock, Hotel


def list_beach(request):
    beachs = Beach.objects.all()
    context = {'beachs': beachs}
    return render(request, 'sunrise/beach/list.html', context)

def detail_beach(request, beach):
    beach = get_object_or_404(Beach, slug= beach)
    context = {'beach': beach}
    return render(request, 'sunrise/beach/detail.html', context)

    
