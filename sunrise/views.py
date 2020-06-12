from django.shortcuts import render, get_object_or_404
from .models import Beach, Rock, Hotel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def list_beach(request):
    beachs_all = Beach.objects.all()
    paginator = Paginator(beachs_all, 10)
    page = request.GET.get('page')
    try:
        beachs = paginator.page(page)
    except PageNotAnInteger:
        beachs = paginator.page(1)
    except EmptyPage:
        beachs = paginator.page(paginator.num_pages)
    context = {'page': page, 'beachs': beachs}
    return render(request, 'sunrise/beach/list.html', context)

def detail_beach(request, beach):
    beach = get_object_or_404(Beach, slug= beach)
    context = {'beach': beach}
    return render(request, 'sunrise/beach/detail.html', context)
