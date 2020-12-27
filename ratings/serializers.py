from rest_framework_mongoengine import serializers
from ratings.models import Ratings


class RatingsSerializer(serializers.DocumentSerializer):
    def __init__(self, *args, **kwargs):
        super(RatingsSerializer, self).__init__(*args, **kwargs)
        self.fields['_id'].read_only = False

    class Meta:
        model = Ratings
        fields = "__all__"
