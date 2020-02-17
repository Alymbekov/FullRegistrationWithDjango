from django.db import models
from apps.users.models import User

class Band(models.Model):
    name = models.CharField(max_length=100)
    foundation_year = models.PositiveSmallIntegerField()
    foundation_city = models.CharField(
        max_length=100, blank=True, null=True
        )
    
    def __str__(self):
        return self.name 

class Album(models.Model):
    name = models.CharField(max_length=255)
    release_year = models.PositiveSmallIntegerField()
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}-{self.band}-{self.release_year}"

    @staticmethod
    def get_old_albums():
        return Album.objects.filter(release_year__lte=2000)


class Track(models.Model):
    name = models.CharField(max_length=100)
    album = models.ForeignKey(
        Album, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='tracks', 
    )
    is_single = models.BooleanField(default=False)
    band = models.ForeignKey(
        Band, on_delete=models.CASCADE,
        related_name='tracks'
    )

    def __str__(self):
        return f'{self.name}-{self.band}'


class InstagramPost(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='instagramposts')

    def __str__(self):
        return self.name
    



class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name + self.last_name
    

class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author) 

    def __str__(self):
        return self.name
    
