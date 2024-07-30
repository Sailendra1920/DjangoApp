from django.db import models
from django.utils import timezone

# Create your models here.
class Username(models.Model):
    CHOICE = [ ('M', 'MALE'), ('F', 'FEMALE')]
    name =  models.CharField(max_length = 100, verbose_name = "Name")
    gender = models.CharField(max_length = 2, choices = CHOICE, verbose_name = "Gender")

    def __str__(self):
        return self.name