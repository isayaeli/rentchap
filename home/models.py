from django.db import models

# Create your models here.
GENDER = (
    ('Male','Male'),
    ('Female','Female')
)
class Team(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.FileField(upload_to='team_images')
    gender = models.CharField(max_length=100, choices=GENDER)
    linkedin = models.URLField(max_length=255, null=True,blank=True)
    twitter = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name