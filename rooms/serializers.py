from rest_framework_mongoengine import serializers
from rooms.models import Rooms


class RoomsSerializer(serializers.DocumentSerializer):

    class Meta:
        model = Rooms
        fields = "__all__"
