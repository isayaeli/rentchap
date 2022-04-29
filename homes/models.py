from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

HOUSE_TYPE = (
    ('Rent','Rent'),
    ('Sale','Sale')
)

KITCHEN = (
    ('Available','Available'),
    ('Not available', 'Not Available')
)
class House(models.Model):
    poste_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    rent = models.CharField(max_length=100)
    area = models.CharField(max_length=100,null=True, blank=True)
    bedroom = models.CharField(max_length=100, null=True, blank=True)
    bathroom = models.CharField(max_length=100, null=True, blank=True)
    parking = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100,null=True, blank=True)
    kitchen = models.CharField(max_length=100, choices=KITCHEN, null=True)
    details = models.TextField()
    house_type = models.CharField(choices=HOUSE_TYPE, max_length=100)
    image = models.FileField(upload_to='house_images')
    published_on = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title


