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
  
