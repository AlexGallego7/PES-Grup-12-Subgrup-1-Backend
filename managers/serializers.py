from rest_framework_mongoengine import serializers
from .models import Managers


class ManagersSerializer(serializers.DocumentSerializer):
    def __init__(self, *args, **kwargs):
        super(ManagersSerializer, self).__init__(*args, **kwargs)
        self.fields['_id'].read_only = False

    class Meta:
        model = Managers
        fields = "__all__"
