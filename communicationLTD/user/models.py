from django.db import models
from django.db.models import CharField

# Create your models here.
class User(models.Model):

    GENDER_CHOICES = (("1", "male"), ("2", "female"), ("3", "other"))
    PLAN_CHOICES = (("1", "2GB"), ("2", "5GB"), ("3", "10GB"), ("4", "50GB"), ("5", "100GB"))

    _id = models.AutoField
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.TextField(choices=GENDER_CHOICES)
    email = models.CharField(max_length=100)
    password1 = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30)
    plan = models.TextField(choices=PLAN_CHOICES)

    def __str__(self) -> CharField:
        return self._id
