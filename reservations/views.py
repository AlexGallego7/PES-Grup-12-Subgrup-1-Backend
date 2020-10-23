from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from reservations.models import Reservations
from reservations.serializers import ReservationsSerializer


class ReservationsView(APIView):

    @staticmethod
    def get(request):
        serializer = ReservationsSerializer(Reservations.objects.all(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request):
        serializer = ReservationsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class ReservationView(APIView):

    def get(self, request, *args, **kwargs):
        reservation_id = self.kwargs['id']
        serializer = ReservationsSerializer(Reservations.objects.filter(_id=reservation_id), many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        reservation_id = self.kwargs['id']
        try:
            Reservations.objects.get(_id=reservation_id).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Reservations.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

