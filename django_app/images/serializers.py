from rest_framework import serializers
from db.models import Images, Comment


class ImageSerializer(serializers.Serializer):

    class Meta:
        model = Images
        fields = '__all__'


class CommentSerializer(serializers.Serializer):

    class Meta:
        model = Comment
        fields = '__all__'
