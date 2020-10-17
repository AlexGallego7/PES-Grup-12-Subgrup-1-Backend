from rest_framework_mongoengine import serializers
from tutorials.models import Tutorial


class TutorialSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published')