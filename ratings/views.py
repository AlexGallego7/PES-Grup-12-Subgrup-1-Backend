from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from events.models import Events
from events.serializers import EventsSerializer
from ratings.models import Ratings
from ratings.serializers import RatingsSerializer


class ManagersView(APIView):

    @staticmethod
    def get(request):
        serializer = RatingsSerializer(Ratings.objects.all(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request):
        serializer = RatingsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.save():
            number_of_ratings = Ratings.objects.get(id_event=serializer.data['id_event'])
            event = Events.objects.get(_id=serializer.data['id_event']).rating
            current_rate = event.rating
            if current_rate is None:
                current_rate = 0
            event.rating = (current_rate + serializer.data.rate) / number_of_ratings
            eserializer = EventsSerializer(event)
            eserializer.is_valid(raise_exception=True)
            eserializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class RatingView(APIView):

    def get(self, request, *args, **kwargs):
        serializer = RatingsSerializer(Ratings.objects.filter(_id=self.kwargs['id']), many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)