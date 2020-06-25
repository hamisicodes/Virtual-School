from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.
#class Profile(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)

    #image = models.ImageField(default='default.jpg', upload_to='profile_pics/')
    #contacts=models.CharField(max_length=50 ,blank=True,null=True)
    #bio=models.CharField(max_length=100,blank=True,null=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

