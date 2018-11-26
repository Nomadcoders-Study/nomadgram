from rest_framework import serializers
from db.models import Images


class ImageSerializer(serializers.Serializer):

    class Meta:
        model = Images
        fields = '__all__'

