from rest_framework_mongoengine import serializers
from applies.models import Applies


class AppliesSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Applies
        fields = "__all__"
