from django.db import models
from django.utils.translation import ugettext_lazy as _
from api.models import User


class Job(models.Model):
    title = models.CharField(max_length=50)
    hourly_rate = models.FloatField(default=15.00)
    company = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    description = models.TextField(max_length=5000)
    contact_email = models.EmailField(_('email address'))
    stylist = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applied_jobs")


