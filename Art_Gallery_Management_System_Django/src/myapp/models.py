from django.db import models
import os
from django.contrib.auth import get_user_model
from datetime import datetime
# Create your models here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

User = get_user_model()


# Artist
class Artist(models.Model):

    artist_name = models.CharField(max_length=300, null=False, blank=False)
    speciality = models.CharField(max_length=300, null=False, blank=False)

# Art


class Art(models.Model):
    art_name = models.CharField(max_length=50, null=False, blank=False)
    art_artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media')
    price = models.FloatField(null=False, blank=False)
    instock = models.BooleanField(null=False, blank=False, default=True)
    description = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.art_name

# TAGs
class Tag(models.Model):

    tag = models.CharField(max_length=300, null=False)
    artid = models.ForeignKey(Art, on_delete=models.CASCADE)

    def __str__(self):
        return self.tag

# Cart Table
class MyCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    art_id = models.ForeignKey(Art, on_delete=models.CASCADE)
    added_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.user


# Order Table


class MyOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    art_id = models.ForeignKey(Art, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.user
    

