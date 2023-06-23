from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify


class PlateModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    license_plate = models.CharField(max_length=255, blank=True)
    brand = models.CharField(max_length=255, blank=True)
    color = models.CharField(max_length=255, blank=True)    
    description = models.TextField(blank=True)
    slug = models.SlugField(null = True, unique = True, max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='plate/', blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.license_plate
    
    def get_absolute_url(self):
        return reverse('plate:plate', kwargs={'slug': self.slug })

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.license_plate)
        return super().save(*args, **kwargs)
