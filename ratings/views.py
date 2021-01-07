from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from events.models import Events
from events.serializers import EventsSerializer
from ratings.models import Ratings
from ratings.serializers import RatingsSerializer
from reservations.models import Reservations
from reservations.serializers import ReservationsSerializer


class RatingsView(APIView):

    @staticmethod
    def get(request):
        serializer = RatingsSerializer(Ratings.objects.all(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request):
        request.data['_id'] = request.user.username + "_" + request.data['id_event']
        serializer = RatingsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.save():
            ratings = RatingsSerializer(Ratings.objects.filter(id_event=serializer.data['id_event']), many=True)
            number_of_ratings = len(ratings.data)
            event = EventsSerializer(Events.objects.get(_id=serializer.data['id_event'])).data.copy()
            if event['ratings'] is None:
                event['ratings'] = serializer.data["rate"]
            else:
                event['ratings'] = (event['ratings'] + serializer.data["rate"]) / number_of_ratings
            eserializer = EventsSerializer(data=event)
            eserializer.is_valid(raise_exception=True)
            if eserializer.save():
                reservation = ReservationsSerializer(
                    Reservations.objects.get(_id=request.data['id_event'] + "_" + str(request.user.id))).data.copy()
                reservation['id_review'] = serializer.data["_id"]
                rserializer = ReservationsSerializer(data=reservation)
                rserializer.is_valid(raise_exception=True)
                rserializer.save()

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class RatingView(APIView):

    def get(self, request, *args, **kwargs):
        serializer = RatingsSerializer(Ratings.objects.filter(_id=self.kwargs['id']), many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        rating_id = self.kwargs['id']
        try:
            rating = Ratings.objects.get(_id=rating_id)
        except Events.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        number_of_ratings = len(RatingsSerializer(Ratings.objects.filter(id_event=rating.id_event), many=True).data)
        event = EventsSerializer(Events.objects.get(_id=rating.id_event)).data.copy()
        event['ratings'] -= rating.rate
        event['ratings'] = (event['ratings'] + request.data["rate"]) / number_of_ratings
        eserializer = EventsSerializer(data=event)
        eserializer.is_valid(raise_exception=True)
        eserializer.save()
        serializer = RatingsSerializer(rating, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)


class EventRatings(APIView):

    def get(self, request, *args, **kwargs):
        serializer = RatingsSerializer(Ratings.objects.filter(id_event=self.kwargs['event']), many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
