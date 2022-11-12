from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):
    """Manager for user"""
    def create_user(self, email, username, password, role, avatar, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,username=username,role=role,avatar=avatar,**extra_fields)
        user.set_password(password)
        user.save()
        return user


class AuthUser(AbstractBaseUser, PermissionsMixin):
    ROLES = (
        (1, 'Super Admin'),
        (2, 'Normal User'),
        (3, 'Artist')
    )
    email = models.EmailField(max_length=255, unique=True)
    role = models.IntegerField(choices=ROLES, default=2)
    avatar = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role']