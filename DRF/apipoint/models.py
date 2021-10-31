from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models

# Пользователь
class CustomUser(AbstractUser):
    image = models.ImageField('Фото', upload_to='users_images', blank=True, null=True)
    email = models.EmailField('Email', max_length=254, unique=True, null=True)
    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=30)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    def __str__(self):
        return self.email
