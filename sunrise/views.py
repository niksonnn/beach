from django.shortcuts import render, get_object_or_404
from .models import Beach, Rock, Hotel, CommentBeach, CommentRock, CommentHotel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailForm, BeachCommentForm, RockCommentForm, HotelCommentForm
from taggit.models import Tag

def list_beach(request, tag_slug = None):
    beachs_all = Beach.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    paginator = Paginator(beachs_all, 10)
    page = request.GET.get('page')
    try:
        beachs = paginator.page(page)
    except PageNotAnInteger:
        beachs = paginator.page(1)
    except EmptyPage:
        beachs = paginator.page(paginator.num_pages)
    context = {'page': page, 'beachs': beachs, 'tag':tag}
    return render(request, 'sunrise/beach/list.html', context)

def detail_beach(request, beach):
    beach = get_object_or_404(Beach, slug= beach)
    comments = beach.comments.all()
    new_comment = None
    if request.method == 'POST':
        comment_form = BeachCommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.beach = beach
            new_comment.save()
    else:
        comment_form = BeachCommentForm()
    context = {'beach': beach, 'comments': comments, 'new_comment': new_comment,
                                    'comment_form': comment_form}
    return render(request, 'sunrise/beach/detail.html', context)

def list_rock(request, tag_slug = None):
    rock_all = Rock.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    paginator = Paginator(rock_all, 10)
    page = request.GET.get('page')
    try:
        rocks = paginator.page(page)
    except PageNotAnInteger:
        rocks = paginator.page(1)
    except EmptyPage:
        rocks = paginator.page(paginator.num_pages)
    context = {'page': page, 'rocks': rocks, 'tag':tag}
    return render(request, 'sunrise/rock/listrock.html', context)

def detail_rock(request, rock):
    rock = get_object_or_404(Rock, slug= rock)
    comments = rock.comments.all()
    new_comment = None
    if request.method == 'POST':
        comment_form = RockCommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.rock = rock
            new_comment.save()
    else:
        comment_form = RockCommentForm()
    context = {'rock': rock, 'comments': comments, 'new_comment': new_comment,
                                                'comment_form': comment_form,}
    return render(request, 'sunrise/rock/detailrock.html', context)

def list_hotel(request, tag_slug = None):
    hotel_all = Hotel.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    paginator = Paginator(hotel_all, 10)
    page = request.GET.get('page')
    try:
        hotels = paginator.page(page)
    except PageNotAnInteger:
        hotels = paginator.page(1)
    except EmptyPage:
        hotels = paginator.page(paginator.num_pages)
    context = {'page': page, 'hotels': hotels, 'tag':tag}
    return render(request, 'sunrise/hotel/listhotel.html', context)

def detail_hotel(request, hotel):
    hotel = get_object_or_404(Hotel, slug= hotel)
    comments = hotel.comments.all()
    new_comment = None
    if request.method == 'POST':
        comment_form = HotelCommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.hotel = hotel
            new_comment.save()
    else:
        comment_form = HotelCommentForm()
    context = {'hotel': hotel, 'comments': comments, 'new_comment': new_comment,
                                            'comment_form': comment_form,}
    return render(request, 'sunrise/hotel/detailhotel.html', context)

def mess(request):
    form = EmailForm()
    flug = False
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            message = "Message"
        send_message(message, 'email@mail.ru', cd['to_email'])
        flug = True
    else:
        form = EmailForm()
        context ={'form': form, 'flug': flug}
    return render(request, 'sunrise/mess.html', context)
