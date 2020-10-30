from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from measures.models import Measures
from measures.serializers import MeasuresSerializer


class MeasuresView(APIView):

    @staticmethod
    def get(request):
        serializer = MeasuresSerializer(Measures.objects.all(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request):
        serializer = MeasuresSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class MeasureView(APIView):

    def get(self, request, *args, **kwargs):
        measure_name = self.kwargs['name']
        serializer = MeasuresSerializer(Measures.objects.filter(name=measure_name), many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        measure_name = self.kwargs['name']
        try:
            Measures.objects.get(name=measure_name).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Measures.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
