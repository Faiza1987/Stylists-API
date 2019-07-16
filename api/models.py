from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=10)
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='profile')

    phone_number = models.CharField(max_length=10)
    years_experience = models.IntegerField(default=0)
    licenses = models.FileField(upload_to='uploads', blank=True)
    photo1 = models.ImageField(upload_to='uploads', blank=True)
    photo2 = models.ImageField(upload_to='uploads', blank=True)
    photo3 = models.ImageField(upload_to='uploads', blank=True)
    photo4 = models.ImageField(upload_to='uploads', blank=True)
    photo5 = models.ImageField(upload_to='uploads', blank=True)
    photo6 = models.ImageField(upload_to='uploads', blank=True)
    specializations = models.TextField(max_length=1000)






