from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from events.models import Events
from events.serializers import EventsSerializer


class EventsView(APIView):

    @staticmethod
    def get(request):
        serializer = EventsSerializer(Events.objects.all(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request):
        serializer = EventsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class EventView(APIView):

    def get(self, request, *args, **kwargs):
        event_id = self.kwargs['id']
        serializer = EventsSerializer(Events.objects.filter(_id=event_id), many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        event_id = self.kwargs['id']
        try:
            Events.objects.get(_id=event_id).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Events.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

