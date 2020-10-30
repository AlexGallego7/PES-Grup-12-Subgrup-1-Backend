from rest_framework_mongoengine import serializers
from measures.models import Measures


class MeasuresSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Measures
        fields = ('name', 'indications')

