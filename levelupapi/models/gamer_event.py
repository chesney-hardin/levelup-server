from django.db import models

class GamerEvent(models.Model):
    event=models.ForeignKey("Event", on_delete=models.CASCADE)
    gamer= models.ForeignKey("Gamer", on_delete=models.CASCADE)
