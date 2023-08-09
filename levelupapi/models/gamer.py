from django.db import models
from django.contrib.auth.models import User

class Gamer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=150)

    @property
    def full_name(self):
        # use an f string 
        return f'{self.user.first_name} {self.user.last_name}'
    