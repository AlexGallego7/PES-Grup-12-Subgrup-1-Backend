from rest_framework_mongoengine import serializers
from rooms.models import Rooms


class RoomsSerializer(serializers.DocumentSerializer):

    def __init__(self, *args, **kwargs):
        super(RoomsSerializer, self).__init__(*args, **kwargs)
        self.fields['_id'].read_only = False

    class Meta:
        model = Rooms
        fields = "__all__"
