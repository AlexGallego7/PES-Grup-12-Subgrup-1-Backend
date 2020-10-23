from rest_framework_mongoengine import serializers
from reservations.models import Reservations


class ReservationsSerializer(serializers.DocumentSerializer):
    def __init__(self, *args, **kwargs):
        super(ReservationsSerializer, self).__init__(*args, **kwargs)
        self.fields['_id'].read_only = False

    class Meta:
        model = Reservations
        fields = "__all__"

