from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from utils.functions import seat_assign
from reservations.models import Reservations
from reservations.serializers import ReservationsSerializer


class ReservationsView(APIView):

    @staticmethod
    def get(request):
        serializer = ReservationsSerializer(Reservations.objects.all(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request, *args, **kwargs):
        if int(request.query_params['n']) > 4:
            return Response({"error": "Due COVID-19 restrictions, we can not assing more than 4 seats"},
                            status=status.HTTP_400_BAD_REQUEST)
        request.data['_id'] = request.data['id_event'] + "_" + str(request.user.id)
        request.data['id_user'] = request.user.id
        seients = seat_assign(request.data['id_event'], request.user.id, request.query_params['n'])
        if len(seients) > 0:
            request.data['seat_number'] = seients
            serializer = ReservationsSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Can not found " + request.query_params['n'] + " available seats"},
                            status=status.HTTP_400_BAD_REQUEST)


class ReservationView(APIView):

    def get(self, request, *args, **kwargs):
        reservation_id = self.kwargs['id']
        try:
            reservation = ReservationsSerializer(Reservations.objects.get(_id=reservation_id))
            return Response(data=reservation.data, status=status.HTTP_200_OK)
        except Reservations.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        reservation_id = self.kwargs['id']
        try:
            Reservations.objects.get(_id=reservation_id).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Reservations.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
