from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, phone, password=None, **extra_fields):
        if not email or not phone:
            raise ValueError('Email or phone is empty')
        
        email = self.normalize_email(email=email)
        user = self.model(email=email, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    

    def create_superuser(self, email, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email=email, phone=phone, password=password, **extra_fields)
    


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    affiliatione = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'phone', 'first_name', 'last_name']


    def __str__(self) -> str:
        return self.email
    

class Member(models.Model):
    name = models.CharField(max_length=150, unique=True)
    job = models.CharField(max_length=150)
    desc = models.TextField()
    img = models.ImageField(upload_to='member/')
    type = models.CharField(max_length=150)


    def __str__(self) -> str:
        return self.name
    

class ConferenceAgenda(models.Model):
    day = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.day


class PartAgenda(models.Model):
    title = models.CharField(max_length=200)
    agend = models.ForeignKey(ConferenceAgenda, related_name='parts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.title
    

class ConferenceSection(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='logo/')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.title