from rest_framework_mongoengine import serializers
from rest_framework import serializers as drf_serializer

from events.models import Events


class EventsSerializer(serializers.DocumentSerializer):

    def __init__(self, *args, **kwargs):
        super(EventsSerializer, self).__init__(*args, **kwargs)
        self.fields['_id'].read_only = False

    class Meta:
        model = Events
        fields = "__all__"

