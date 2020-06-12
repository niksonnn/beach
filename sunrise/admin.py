from django.contrib import admin
from .models import Beach, Rock, Hotel
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
