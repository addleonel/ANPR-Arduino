from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify


class PlateModel(models.Model):
    OPTIONS = [
        ('ADMITED', 'admited'),
        ('BANNED', 'banned'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userplate')
    license_plate = models.CharField(max_length=255, blank=False, null=False, unique=True)
    brand = models.CharField(max_length=255, blank=True)
    color = models.CharField(max_length=255, blank=True)    
    status = models.CharField(max_length=255, blank=True, default='ADMITED', choices=OPTIONS)
    description = models.TextField(blank=True)
    slug = models.SlugField(null = True, unique = True, max_length=300)
    image = models.ImageField(upload_to='img/license_plates/', blank=True, null=True, max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.license_plate
    
    def get_absolute_url(self):
        return reverse('plate:plate', kwargs={'slug': self.slug })

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.license_plate)
        return super().save(*args, **kwargs)


class PlateCapturedModel(models.Model):
    plate = models.CharField(max_length=255, blank=True, null=True)
    image_license = models.ImageField(upload_to='img/plate_captured/', blank=True, null=True, max_length=300)
    image_car = models.ImageField(upload_to='img/car_captured/', blank=True, null=True, max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.plate

    
