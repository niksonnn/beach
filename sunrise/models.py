from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager


class Beach(models.Model):
    #name 	full_name 	address 	phone 	email 	accredited_organization
    #region 	certificate_number 	registrated_num 	inn 	ogrn 	category
    name  = models.CharField(max_length=250, verbose_name = 'Название пляжа')
    full_name = models.TextField(verbose_name = 'Полное название')
    address = models.CharField(max_length=250, verbose_name = 'Адрес')
    phone = models.CharField(max_length=50, verbose_name = 'Телефон')
    email = models.CharField(max_length=250, verbose_name = 'Электронная почта')
    region = models.CharField(max_length=150, verbose_name = 'Регион')
    accredited_organization = models.CharField(max_length=250,
                    verbose_name = 'Организация проводившая аккредитацию')
    certificate_number =models.CharField(max_length=150,
                                        verbose_name = 'Номер сертификата' )
    registrated_num = models.CharField(max_length=150,
                                    verbose_name = 'Регистрационный номер')
    inn = models.IntegerField(verbose_name = 'ИНН')
    ogrn= models.IntegerField(verbose_name = 'ОГРН')
    category = models.CharField(max_length=250, verbose_name = 'Категория')
    slug = models.SlugField(max_length=250)
    tags = TaggableManager()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('sunrise:detail_beach', args=[self.slug])





class Rock(models.Model):
    #name 	full_name 	address 	phone 	email 	accredited_organization
    #region 	certificate_number 	registrated_num 	inn 	ogrn 	category
    name  = models.CharField(max_length=250, verbose_name = 'Название горнолыжной трассы')
    full_name = models.TextField(verbose_name = 'Полное название')
    address = models.CharField(max_length=250, verbose_name = 'Адрес')
    phone = models.CharField(max_length=50, verbose_name = 'Телефон')
    email = models.CharField(max_length=250, verbose_name = 'Электронная почта')
    region = models.CharField(max_length=150, verbose_name = 'Регион')
    accredited_organization = models.CharField(max_length=250,
                    verbose_name = 'Организация проводившая аккредитацию')
    certificate_number =models.CharField(max_length=150,
                                        verbose_name = 'Номер сертификата' )
    registrated_num = models.CharField(max_length=150,
                                    verbose_name = 'Регистрационный номер')
    inn = models.IntegerField(verbose_name = 'ИНН')
    ogrn= models.IntegerField(verbose_name = 'ОГРН')
    category = models.CharField(max_length=250, verbose_name = 'Категория')
    slug = models.SlugField(max_length=250)
    tags = TaggableManager()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sunrise:detail_rock', args=[self.slug])


class Hotel(models.Model):
    #name 	full_name 	address 	phone 	email 	accredited_organization
    #region 	certificate_number 	registrated_num 	inn 	ogrn 	category
    name  = models.CharField(max_length=250, verbose_name = 'Название горнолыжной трассы')
    full_name = models.TextField(verbose_name = 'Полное название')
    address = models.CharField(max_length=250, verbose_name = 'Адрес')
    phone = models.CharField(max_length=50, verbose_name = 'Телефон')
    email = models.CharField(max_length=250, verbose_name = 'Электронная почта')
    region = models.CharField(max_length=150, verbose_name = 'Регион')
    accredited_organization = models.CharField(max_length=250,
                    verbose_name = 'Организация проводившая аккредитацию')
    certificate_number =models.CharField(max_length=150,
                                        verbose_name = 'Номер сертификата' )
    registrated_num = models.CharField(max_length=150,
                                    verbose_name = 'Регистрационный номер')
    inn = models.CharField(max_length=150, verbose_name = 'ИНН')
    ogrn= models.CharField(max_length=150, verbose_name = 'ОГРН')
    category = models.CharField(max_length=250, verbose_name = 'Категория')
    slug = models.SlugField(max_length=250)
    tags = TaggableManager()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sunrise:detail_hotel', args=[self.slug])

class CommentBeach(models.Model):
    #Comments users for Beachs
    beach = models.ForeignKey(Beach, on_delete=models.CASCADE, related_name='comments')
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name = 'Имя')
    email = models.EmailField()
    com = models.TextField(verbose_name = 'Комментарий')
    image = models.ImageField(blank=True, verbose_name = 'Изображение')
    publish = models.DateTimeField(auto_now_add=True, verbose_name = 'Опубликовано' )
    active = models.BooleanField(default = True)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return 'Комментарий от {}'.format(self.name)

class CommentRock(models.Model):
    #Comments users for Rocks
    rock = models.ForeignKey(Rock, on_delete=models.CASCADE,
                related_name='comments')
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name = 'Имя')
    email = models.EmailField()
    com = models.TextField(verbose_name = 'Комментарий')
    image = models.ImageField(blank=True, verbose_name = 'Изображение')
    publish = models.DateTimeField(auto_now_add=True, verbose_name = 'Опубликовано' )
    active = models.BooleanField(default = True)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return 'Комментарий от {}'.format(self.name)

class CommentHotel(models.Model):
    #Comments users for Hotels
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='comments')
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name = 'Имя')
    email = models.EmailField()
    com = models.TextField(verbose_name = 'Комментарий')
    image = models.ImageField(blank=True, verbose_name = 'Изображение')
    publish = models.DateTimeField(auto_now_add=True, verbose_name = 'Опубликовано' )
    active = models.BooleanField(default = True)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return 'Комментарий от {}'.format(self.name)
