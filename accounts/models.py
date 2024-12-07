from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    role = models.CharField(
        max_length=50,
        choices=[('project_member', 'Project Member'), ('project_manager', 'Project Manager')],
        default='project_manager'
    )
    full_name = models.CharField(max_length=255, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class User(models.Model):
    ROLE_CHOICES, default = [
        ('project_member','Project Member'),
        ('project_manager', 'Project Manager')
    ]
    role = models.CharField(max_length=50, default='Not assigned')
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='/statitc/default-profile.jpg')
