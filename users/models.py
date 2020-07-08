from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image',)
    contacts=models.CharField(max_length=50 ,blank=True,null=True)
    bio=models.CharField(max_length=100,blank=True,null=True)
    
    def save_profile(self):
        self.save()

        
    def __str__(self):
        return f'{self.user} Profile'


