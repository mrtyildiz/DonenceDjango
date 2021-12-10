from enum import unique
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.timezone import now
from tinymce.models import HTMLField

Futures  = [
    ('security', 'güvenlik'),
    ('reading', 'okuma'),
    ('diploma', 'diploma'),
    ('education', 'egitim'),
    ('jigsaw', 'yapboz'),
    ('kids', 'cocuk')
]

class Future(models.Model):
    headers = models.CharField(max_length=100, null=True)
    Explanation = models.CharField(max_length=255, null=True)
    month = CharField(max_length=10, choices=Futures, default='security')
    def __str__(self):
        return self.headers  


class footer(models.Model):
    adress = models.CharField(max_length=220, null=False)
    telephone = models.CharField(max_length=12, null=False)
    email = models.EmailField(max_length=254)
    twitter = models.URLField(max_length=254)
    facebook = models.URLField(max_length=254)
    instagram = models.URLField(max_length=254)



#Dersler için oluşturdum
class Course(models.Model):
    name = models.CharField(max_length=50, null=True)
    Courses_time = models.CharField(max_length=50, null=True)
    Courses_explanation = models.CharField(max_length=500, null=True)
    image = models.ImageField(upload_to='Courses')
    Status = models.BooleanField(default=False)
    def __str__(self):
        return self.name


#Galeri upload bölümü
class Galery(models.Model):
    name = models.CharField(max_length=25, null=True)
    AltString = models.CharField(max_length=25, null=True)
    image = models.ImageField(upload_to='Galery')
    def __str__(self):
        return self.name

###Blog 
class Blogs(models.Model):
    Header = models.CharField(max_length=100, null=True)
    Explanation = models.CharField(max_length=255, null=True)
    Date = models.DateTimeField()
    image = models.ImageField(upload_to='Blog')
    lesson = models.FileField(upload_to='pdf')
    def __str__(self):
        return self.Header
#USer bölümü
# Yorum Yapmak için ctrl +k geri almak için ctrl+ö kullan

class teacher(models.Model):
    name = models.CharField(max_length=100, null=True)
    brans = models.CharField(max_length=100, null=True)
    Certificate = models.BooleanField(default=True)
    explanation = models.CharField(max_length=255, null=True)
    twitter = models.URLField(max_length=254)
    facebook = models.URLField(max_length=254)
    instagram = models.URLField(max_length=254)
    image = models.ImageField(upload_to='teacher')
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class ebeveyn(models.Model):
    ebeveynName = models.CharField(max_length=100, null=True)
    studentName = models.CharField(max_length=100, null=True)
    Email = models.EmailField(max_length=254, unique=True)
    Password = models.CharField(max_length=100, null=True)
    Status = models.BooleanField(default=False)

    def __str__(self):
        return self.ebeveynName