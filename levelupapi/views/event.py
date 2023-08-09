from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event, Gamer
from .game import GameSerializer


class EventView(ViewSet):

    def list(self, request):
        """Handle GET requests to get all events
        """
        events = Event.objects.all()
        if "game" in request.query_params:
            pk= request.query_params['game']
            events = events.filter(game = pk)


        serialized = EventSerializer(events, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk):
        """Handle GET requests for single Event 

        Returns:
            Response -- JSON serialized Event 
        """
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class EventOrganizerSerializer(serializers.ModelSerializer):
    """JSON serializer for Events"""
    class Meta:
        model = Gamer
        fields = ('id', 'full_name', 'bio')

class EventAttendeesSerializer(serializers.ModelSerializer):
    """JSON serializer for Events"""
    class Meta:
        model = Gamer
        fields = ('id', 'full_name', 'bio')

class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for Events"""
    game = GameSerializer(many=False)
    organizer = EventOrganizerSerializer(many=False)
    attendees = EventAttendeesSerializer(many=True)
    class Meta:
        model = Event
        fields = ('id', 'organizer', 'game', 'date', 'attendees')

