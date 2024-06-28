from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Users(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(blank=False)
    profile_pic=models.ImageField(upload_to='profile_pics/')
    is_approved=models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
