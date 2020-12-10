from functools import reduce
from operator import or_

from mongoengine import Q
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import MyUser
from accounts.serializers import RegisterSerializer
from clients.models import Clients
from clients.serializers import ClientSerializer
from events.models import Events
from events.serializers import EventsSerializer
from reservations.models import Reservations
from reservations.serializers import ReservationsSerializer


class ClientsView(APIView):

    @staticmethod
    def get(request):
        serializer = ClientSerializer(Clients.objects.all(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request):
        # Comprovem que l'usuari no sigui manager
        if request.data["is_manager"]:
            return Response("A client can not be manager", status=status.HTTP_400_BAD_REQUEST)

        # Creem l'usuari
        user = RegisterSerializer(data=request.data)
        user.is_valid(raise_exception=True)
        user.save()

        # Creem el client amb l'id i l'username de l'usuari
        client = {
            "_id": user.data["id"],
            "username": user.data["username"],
            "age": request.data.get('age', None),
            "country": request.data.get('country', None)}

        serializer = ClientSerializer(data=client)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class ClientView(APIView):

    def get(self, request, *args, **kwargs):
        username = self.kwargs['username']
        serializer = ClientSerializer(Clients.objects.filter(username=username), many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class AgendaView(APIView):

    @staticmethod
    def get(request):
        print(request.user.id)
        serializer = ReservationsSerializer(Reservations.objects.filter(id_user=request.user.id), many=True)
        print(serializer.data)
        reservations = []
        for i in range(len(serializer.data)):
            reservations.append(serializer.data[i]['id_event'])

        print(reservations)

        serializer = EventsSerializer(Events.objects.filter(reduce(or_, [Q(_id=c) for c in reservations])), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

