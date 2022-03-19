from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils import timezone

GENDER_MALE = 'Male'
GENDER_FEMALE = 'Female'
GENDER_CHOICE = (
    (GENDER_MALE, 'Male'),
    (GENDER_FEMALE, 'Female'),
)




class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)



class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True, related_name='teacherProfile')

    # Basic Information
    FirstName = models.CharField(max_length=30, blank=False, null=False, verbose_name='First Name')
    LastName = models.CharField(max_length=30, blank=False, null=False, verbose_name='Last Name')
    Gender = models.CharField(max_length=20,blank=False, choices=GENDER_CHOICE)
    PhoneNumber = models.CharField(max_length=20, blank=True, verbose_name='Phone Number')
    Address = models.CharField(max_length=100, blank=True, verbose_name='Current Address')
    ProfileImage = models.ImageField(default='defaultusers.png', blank=True, upload_to='Teacher/Profiles', verbose_name='Profile Picture')
   




    def __str__(self):
        return f'{self.user.username} profile'


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True, related_name='studentProfile')

    # Basic Information
    FirstName = models.CharField(max_length=30, blank=False, null=False, verbose_name='First Name')
    LastName = models.CharField(max_length=30, blank=False, null=False, verbose_name='Last Name')
    Gender = models.CharField(max_length=20,blank=False, choices=GENDER_CHOICE)
    PhoneNumber = models.CharField(max_length=20, blank=True, verbose_name='Phone Number')
    Address = models.CharField(max_length=100, blank=True, verbose_name='Current Address')
    ProfileImage = models.ImageField(default='defaultusers.png', blank=True, upload_to='Student/Profiles', verbose_name='Profile Picture')
   
   

    def __str__(self):
        return f'{self.user.username} profile'

    

