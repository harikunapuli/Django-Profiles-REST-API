from django.db import models # type: ignore
from django.contrib.auth.models import AbstractBaseUser # type: ignore
from django.contrib.auth.models import PermissionsMixin # type: ignore
from django.contrib.auth.models import BaseUserManager # type: ignore
from django.conf import settings 
# Create your models here.
class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self,email,name,password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("User must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email,name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,name,password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user 

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrive full name of user"""
        return self.name
    def get_short_name(self):
        """Retrive short name of user"""
        return self.name
    def ___str___(self):
        """Return String rpresentation of our user"""
        return self.email
class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.status_text