
from django.db import models
from django.utils import timezone
from phone_field import PhoneField

# Create your models here.
class registration(models.Model):
    email=models.EmailField(max_length=100)
    code=models.CharField(max_length=100)
    pwd=models.CharField(max_length=100)
    currentdate= models.DateField(default=timezone.now)

    def __str__(self):
        return self.email



class stdprofile(models.Model):
    name = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    roll = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    programme=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    sem=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    currentdate= models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.name


class facprofile(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    add = models.CharField(max_length=100)
    spec = models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    currentdate= models.DateField(default=timezone.now)

    def __str__(self):
        return self.name



class subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    currentdate= models.DateField(default=timezone.now)

    def __str__(self):
        return self.name


class subjectallotment(models.Model):
    sname = models.CharField(max_length=100)
    tname = models.CharField(max_length=100)
    programme = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    sem = models.CharField(max_length=100)
    currentdate= models.DateField(default=timezone.now)

    def __str__(self):
        return self.sname



class feedbackreg(models.Model):
    programme = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    sem = models.CharField(max_length=100)
    stdid = models.CharField(max_length=100)
    sname = models.CharField(max_length=100)
    tname = models.CharField(max_length=100)
    currentdate= models.DateField(default=timezone.now)
    ques1 = models.CharField(max_length=100)
    ques2 = models.CharField(max_length=100)
    ques3 = models.CharField(max_length=100)
    ques4 = models.CharField(max_length=100)
    ques5 = models.CharField(max_length=100)
    overall = models.CharField(max_length=100)

    def __str__(self):
        return self.programme



class startfeedback(models.Model):
    programme=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    sem=models.CharField(max_length=100)
    pwd=models.CharField(max_length=100)
    currentdate= models.DateField(default=timezone.now)

    def __str__(self):
        return self.programme



class notes(models.Model):
    sname = models.CharField(max_length=100)
    programme = models.CharField(max_length=20)
    branch = models.CharField(max_length=20)
    sem = models.CharField(max_length=20)
    document = models.FileField(upload_to='books/pdf/', null=True, blank=True)


    def __str__(self):
        return self.sname