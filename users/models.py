from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)

    address = models.CharField(null=True, blank=True, max_length=255)
    city = models.CharField(null=True, blank=True, max_length=30)
    postcode = models.CharField(null=True, blank=True, max_length=10)
    mobile = models.CharField(null=True, blank=True, max_length=15)
    profile_picture = models.ImageField(null=True, blank=True, upload_to="users/profile")
