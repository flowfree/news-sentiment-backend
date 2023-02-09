from __future__ import annotations 

from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    """
    Custom model manager for our custom User model. 
    """
    use_in_migrations = True

    def create_user(
        self, 
        email: str, 
        password: str, 
        **extra_fields: bool
    ) -> User:
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(
        self, 
        email: str, 
        password: str, 
        **extra_fields: bool
    ) -> User:
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self._create_user(email, password, **extra_fields)

    def _create_user(
        self, 
        email: str, 
        password: str, 
        **extra_fields: bool
    ) -> User:
        if not email:
            raise ValueError('Please specify the email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
