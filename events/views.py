from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from events.models import Events
from events.serializers import EventsSerializer
from utils.functions import create_matrix, string_to_matrix, matrix_to_string


class EventsView(APIView):

    @staticmethod
    def get(request):
        if request.user.id is not None and request.user.is_manager:
            serializer = EventsSerializer(Events.objects.filter(id_manager=request.user.id), many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            serializer = EventsSerializer(Events.objects.all(), many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request):
        request.data['seats'] = matrix_to_string(create_matrix(request.data["id_room"]))
        serializer = EventsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class EventView(APIView):

    def get(self, request, *args, **kwargs):
        event_id = self.kwargs['id']
        serializer = EventsSerializer(Events.objects.get(_id=event_id))
        data = serializer.data.copy()
        data['matrix'] = string_to_matrix(serializer.data['seats'])
        return Response(data=data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        event_id = self.kwargs['id']
        try:
            event = Events.objects.get(_id=event_id)
        except Events.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = EventsSerializer(event, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        event_id = self.kwargs['id']
        try:
            Events.objects.get(_id=event_id).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Events.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
