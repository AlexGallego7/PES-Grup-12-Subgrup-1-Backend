from rest_framework_mongoengine import serializers
from events.models import Events


class EventsSerializer(serializers.DocumentSerializer):

    class Meta:
        model = Events
        fields = "__all__"

