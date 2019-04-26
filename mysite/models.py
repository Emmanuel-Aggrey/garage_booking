from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Servicings(models.Model):
    service_type = models.CharField(max_length=50)
    service_isPaid = models.CharField(max_length=50)
    service_description = models.TextField(null=True)
    service_location = models.CharField(max_length=50, blank=True, null=True)
    service_booked = models.DateTimeField(auto_now_add=True)
    service_modified = models.DateTimeField(auto_now=True)
    service_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Service No - ' + str(self.id)

    def get_absolute_url(self):
        return reverse('dashboard')