from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

User._meta.get_field('email')._unique = True

class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    photo = models.ImageField()

    def __str__(self):
        return self.user.username