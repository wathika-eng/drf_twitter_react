from django.db import models


# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=20, blank=False)
    bio = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.name


class Advocate(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.SET_NULL, null=True, blank=True
    )
    profile_pic = models.ImageField(
        upload_to="images/",
        null=True,
        blank=True,
        default="https://randomuser.me/api/portraits/men/1.jpg",
    )
    username = models.CharField(max_length=30, blank=False)
    bio = models.TextField(max_length=40, null=True, blank=True)

    def __str__(self):
        return f"{self.username} - {self.company} {self.bio} {self.profile_pic}"


# >>> from drfapi.models import Advocate, Company
# >>> advocates = Advocate.objects.all()
# >>> advocates
