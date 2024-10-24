"""
User models.
"""
import os
import uuid
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)  # normalize_email method is provied by BaseUserManager
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

def profile_pic_path(instance, filename):
    """Generate file path for new profile image."""
    ext = os.path.splitext(filename)[1] # extension like png / jpg etc
    filename = f'{uuid.uuid4()}{ext}'
    return os.path.join('uploads', str(instance.id), filename)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, unique=True)
    # bio = models.CharField(max_length=255, blank=True)
    # location = models.CharField(max_length=255, blank=True)
    # profile_pic = models.ImageField(upload_to=profile_pic_path, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    # def profile(self):
    #     profile = Profile

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    bio = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    profile_pic = models.ImageField(upload_to=profile_pic_path, blank=True)

    def __str__(self):
        return self.full_name