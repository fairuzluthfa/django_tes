from django.db import models

# Create your models here.
# from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.description


# from django.db import models
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name}-{self.last_name}'





class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __str__(self):
        return f'{self.name}-{self.artist.first_name}'