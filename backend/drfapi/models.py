from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.hashers import make_password
from .manager import AdvocateManager

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=20, blank=False)
    bio = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.name


class Advocate(AbstractBaseUser, PermissionsMixin):
    company = models.ForeignKey(
        Company, on_delete=models.SET_NULL, null=True, blank=True
    )
    profile_pic = models.ImageField(
        upload_to="images/",
        null=True,
        blank=True,
        default="https://randomuser.me/api/portraits/men/1.jpg",
    )
    username = models.CharField(max_length=30, unique=True, blank=False)
    bio = models.TextField(max_length=40, null=True, blank=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = AdvocateManager()

    def __str__(self):
        return f"{self.username} - {self.company} {self.bio} {self.profile_pic}"


# >>> from drfapi.models import Advocate, Company
# >>> advocates = Advocate.objects.all()
# >>> advocates
