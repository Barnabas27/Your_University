from django.db import models
from cloudinary.models import CloudinaryField
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
# Create your models here.
class Courses(models.Model):
    # name = models.CharField(max_length=100, blank=False)
    # description = models.TextField(blank=False)
    Bachelors_in_Computer_Science = 'BCompSc'
    Business_School = 'Business'
    Engineering_School ='Engineering'
    Health_Science = 'Medicine'
    Course_choices = [
        (Bachelors_in_Computer_Science,'BCompSc'),
        (Business_School,'Business'),
        (Engineering_School,'Engineering'),
        (Health_Science,'Medicine'),
    ]
    Course_choices = models.CharField(
        max_length=15,
        choices=Course_choices,
        default=Health_Science,
    )
class Students(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length = 100)
    bio = models.CharField(max_length=255)
    email = models.TextField()
    phone_number=PhoneNumberField(blank=True)
    courses = models.ForeignKey(Courses,on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def save_student(self):
        self.save()
        
    def delete_student(self):
        self.delete()
        
    @classmethod
    def update_bio(cls,id,bio):
        update_profile = cls.objects.filter(id = id).update(bio =bio)
        return update_profile
    
    
    
class Tutor(models.Model):
    name = models.CharField(max_length = 100)
    image = CloudinaryField('image')
    # accolades=models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
    email = models.TextField(blank=True)
    courses = models.ForeignKey(Courses,on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def save_tutor(self):
        self.save()
        
    def delete_tutor(self):
        self.delete()
        
    @classmethod
    def update_bio(cls,id,bio):
        update_profile = cls.objects.filter(id = id).update(bio =bio)
        return update_profile
    
    @classmethod
    def get_all_profiles(cls):
        students = Students.objects.all()
        return profile
    
    @classmethod
    def search_user(cls,user):
        return cls.objects.filter(user__username__icontains = user).all()
    
    
    
