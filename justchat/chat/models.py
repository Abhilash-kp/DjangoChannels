from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ButtonTracker(models.Model):
    fatbuttonclicks = models.IntegerField(default=0)
    stupidbuttonclicks = models.IntegerField(default=0)
    dumbbuttonclicks = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)

