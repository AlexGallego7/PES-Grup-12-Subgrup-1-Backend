from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from rooms.models import Rooms
from rooms.serializers import RoomsSerializer


class RoomsView(APIView):

    @staticmethod
    def get(request):
        serializer = RoomsSerializer(Rooms.objects.filter(id_manager=request.user.id), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request):
        serializer = RoomsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class RoomView(APIView):

    def get(self, request, *args, **kwargs):
        room_id = self.kwargs['id']
        serializer = RoomsSerializer(Rooms.objects.filter(_id=room_id), many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        room_id = self.kwargs['id']
        try:
            room = Rooms.objects.get(_id=room_id)
        except Rooms.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = RoomsSerializer(room, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        room_id = self.kwargs['id']
        try:
            Rooms.objects.get(_id=room_id).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Rooms.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
