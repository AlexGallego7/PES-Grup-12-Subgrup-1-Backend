from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import RegisterSerializer
from managers.models import Managers
from managers.serializers import ManagersSerializer


class ManagersView(APIView):

    @staticmethod
    def get(request):
        serializer = ManagersSerializer(Managers.objects.all(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request):
        # Comprovem que l'usuari no sigui manager
        if not request.data["is_manager"]:
            return Response("A manager can not be client", status=status.HTTP_400_BAD_REQUEST)

        # Creem l'usuari
        user = RegisterSerializer(data=request.data)
        user.is_valid(raise_exception=True)
        user.save()

        # Creem el manager amb l'id i l'username de l'usuari
        manager = {
            "_id": user.data["id"],
            "username": user.data["username"],
            "nif": request.data.get("nif", None),
            "telf": request.data.get("telf", None)}

        serializer = ManagersSerializer(data=manager)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class ManagerView(APIView):

    def get(self, request, *args, **kwargs):
        username = self.kwargs['username']
        serializer = ManagersSerializer(Managers.objects.filter(username=username), many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)