from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

ROLES = (
    (1, 'Super Admin'),
    (2, 'Normal User'),
    (3, 'Artist')
)

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
    """AuthUser class in the system"""
    email = models.EmailField(max_length=255, unique=True)
    role = models.IntegerField(choices=ROLES, default=2)
    avatar = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role']
    
class PremiumPlan(models.Model):
    """PremiumPlan class in the system"""
    type = models.CharField(max_length=255)
    duration = models.IntegerField()
    
class NormalUser(AuthUser):
    """NormalUser class in the system"""
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    auth_user = models.OneToOneField(
        AuthUser,
        on_delete=models.CASCADE,
        related_name="normal_user",
        primary_key=True,
        parent_link=True,
    )
    premium_plan = models.ForeignKey(PremiumPlan, on_delete=models.RESTRICT , null=True)
    premium_plan_updated_at = models.DateTimeField(null=True)

    def get_role(self):
        return ROLES[1]
class SuperAdmin(AuthUser):
    """SuperAdmin class in the system"""
    auth_user = models.OneToOneField(
        AuthUser,
        on_delete=models.CASCADE,
        related_name="super_admin",
        primary_key=True,
        parent_link=True,
    )

    def get_role(self):
        return ROLES[0]
    
class Following(models.Model):
    """Following class in the system"""
    auth_user_follower = models.ForeignKey(AuthUser, related_name='follower', on_delete=models.CASCADE)
    auth_user_following = models.ForeignKey(AuthUser, related_name='following', on_delete=models.CASCADE)