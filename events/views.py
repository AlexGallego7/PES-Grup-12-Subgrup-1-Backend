from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from events.models import Events
from events.serializers import EventsSerializer


class EventsView(APIView):

    def get(self, request):
        serializer = EventsSerializer(Events.objects.all(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EventsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class EventView(APIView):

    def get(self, request, *args, **kwargs):
        name = self.kwargs['name']
        serializer = EventsSerializer(Events.objects.filter(name=name), many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)