from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game


class GameView(ViewSet):

    def list(self, request):
        """Handle GET requests to get all games
        """

        games = Game.objects.all()
        serialized = GameSerializer(games, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk):
        """Handle GET requests for single game 

        Returns:
            Response -- JSON serialized game 
        """
        game = Game.objects.get(pk=pk)
        serializer = GameSerializer(game)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for Games"""
    class Meta:
        model = Game
        fields = ('id', 'name', 'creator', 'game_type', 'number_of_players', 'skill_level')

