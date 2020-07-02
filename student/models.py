from django.db import models
from django.contrib.auth.models import User
from content_management_system.models import Course



class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    image = models.ImageField(default ='default.jpeg', upload_to='profile_pics')
    bio = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    @property
    def number_of_enrollments(self):
        return Enrollment.objects.filter(user=self).count()

    def __str__(self):
        return f'{self.user.username}'


