from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    #required by the auth model
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=30, null=True, blank=True)
