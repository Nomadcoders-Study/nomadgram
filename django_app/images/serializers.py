from rest_framework import serializers
from db.models import Images, Comment, Like


class ImageSerializer(serializers.Serializer):

    class Meta:
        model = Images
        fields = '__all__'


class CommentSerializer(serializers.Serializer):

    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(serializers.Serializer):

    class Meta:
        model = Like
        fields = '__all__'
