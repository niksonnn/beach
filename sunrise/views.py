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

def list_rock(request):
    rock_all = Rock.objects.all()
    paginator = Paginator(rock_all, 10)
    page = request.GET.get('page')
    try:
        rocks = paginator.page(page)
    except PageNotAnInteger:
        rocks = paginator.page(1)
    except EmptyPage:
        rocks = paginator.page(paginator.num_pages)
    context = {'page': page, 'rocks': rocks}
    return render(request, 'sunrise/rock/listrock.html', context)

def detail_rock(request, rock):
    rock = get_object_or_404(Rock, slug= rock)
    context = {'rock': rock}
    return render(request, 'sunrise/rock/detailrock.html', context)

def list_hotel(request):
    hotel_all = Hotel.objects.all()
    paginator = Paginator(hotel_all, 10)
    page = request.GET.get('page')
    try:
        hotels = paginator.page(page)
    except PageNotAnInteger:
        hotels = paginator.page(1)
    except EmptyPage:
        hotels = paginator.page(paginator.num_pages)
    context = {'page': page, 'hotels': hotels}
    return render(request, 'sunrise/rock/listhotel.html', context)

def detail_rock(request, hotel):
    rock = get_object_or_404(Hotel, slug= rock)
    context = {'hotel': hotel}
    return render(request, 'sunrise/rock/detailhotel.html', context)
