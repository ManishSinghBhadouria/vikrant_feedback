
from django.db import models
from django.utils import timezone
from phone_field import PhoneField

# Create your models here.
class registration(models.Model):
    email=models.EmailField(max_length=100)
    mobile=PhoneField(blank=True, help_text='Contact phone number')
    pwd=models.CharField(max_length=100)

    def __str__(self):
        return self.email