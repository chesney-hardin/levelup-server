from django.db import models

class Game(models.Model):    
    creator=models.ForeignKey("Gamer", on_delete=models.SET_NULL, null=True, related_name='created_games')
    game_type= models.ForeignKey("GameType", on_delete=models.DO_NOTHING, related_name='games')
    name = models.CharField(max_length=55)
    number_of_players = models.PositiveSmallIntegerField()
    skill_level = models.CharField(max_length=55)

