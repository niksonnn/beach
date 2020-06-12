from django.contrib import admin
from .models import Beach, Rock, Hotel, CommentBeach, CommentRock, CommentHotel
# Register your models here.

@admin.register(Beach)
class BeachAdmin(admin.ModelAdmin):
    list_display  = ('name', 'slug',  'region', 'address',
                       'category')
    list_filter = ('category', 'region', 'name')
    search_fields = ('name', 'region', 'category', 'ogrn', 'inn')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name', 'category',)

@admin.register(Rock)
class RockAdmin(admin.ModelAdmin):
    list_display  = ('name', 'slug',  'region', 'address',
                       'category')
    list_filter = ('category', 'region', 'name')
    search_fields = ('name', 'region', 'category', 'ogrn', 'inn')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name', 'category',)

    @admin.register(Hotel)
    class HotelAdmin(admin.ModelAdmin):
        list_display  = ('name', 'slug',  'region', 'address',
                           'category')
        list_filter = ('category', 'region', 'name')
        search_fields = ('name', 'region', 'category', 'ogrn', 'inn')
        prepopulated_fields = {'slug': ('name',)}
        ordering = ('name', 'category',)


@admin.register(CommentBeach)
class BeachCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'publish')
    list_filter = ( 'publish',)
    search_fields = ('name', 'email', 'com', 'beach')

@admin.register(CommentRock)
class RockCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'publish')
    list_filter = ( 'publish',)
    search_fields = ('name', 'email', 'com', 'rock')


@admin.register(CommentHotel)
class HotelCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'publish')
    list_filter = ( 'publish',)
    search_fields = ('name', 'email', 'com', 'hotel') 
