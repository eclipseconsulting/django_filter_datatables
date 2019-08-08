from django.db import models
from django.shortcuts import reverse


class Customer(models.Model):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    phone = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    def get_absolute_url(self):
        return reverse('customers:customer_detail', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('customers:customer_delete', kwargs={'pk': self.pk})
