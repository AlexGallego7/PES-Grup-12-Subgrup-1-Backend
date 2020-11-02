from rest_framework_mongoengine import serializers
from .models import Clients


class ClientSerializer(serializers.DocumentSerializer):
    def __init__(self, *args, **kwargs):
        super(ClientSerializer, self).__init__(*args, **kwargs)
        self.fields['_id'].read_only = False

    class Meta:
        model = Clients
        fields = "__all__"

