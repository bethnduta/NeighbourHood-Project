import email
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from PIL import Image



# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='nt.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=100, default='')

    def __str__(self):
        return f'{self.user.username} Profile' 

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})  


class NeighborHood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    occupants = models.IntegerField(default=0)
    description = models.TextField(default='')
    admin= models.ForeignKey(User, on_delete=models.CASCADE)
    police_number = models.IntegerField(default=0)
    health_number = models.IntegerField(default=0)
    image = models.ImageField(default='nt.jpg', upload_to='neighborhood_pics')

    def __str__(self):
        return self.name

    class meta:
        ordering = ['-pk']   

    def create_neighborhood(self):
        self.save()

    def update_neighborhood(self):
        self.update()
        
    def update_occupants(self):
        self.occupants += 1
        self.save()

    def delete_neighborhood(self):
        self.delete() 

    @classmethod
    def find_neighborhood(cls, id):
        neighborhood = cls.objects.filter(id=id)
        return neighborhood 
  
class Business(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='')
    location = models.CharField(max_length=100)
    occupants = models.IntegerField(default=0)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='nt.jpg', upload_to='business_pics')
    email = models.EmailField(default='')
    NeighborHood = models.ForeignKey(NeighborHood, on_delete=models.CASCADE)


class user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='nt.jpg', upload_to='user_pics')
    bio = models.TextField(max_length=100, default='')
    email = models.EmailField(default='')
    NeighborHood = models.ForeignKey(NeighborHood, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username} Profile' 

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})    

