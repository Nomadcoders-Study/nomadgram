from rest_framework import serializers
from db.models import Image, Comment, Like

__all__ = (
    'ImageSerializer',
    'CommentSerializer',
    'LikeSerializer',
)


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = (
            'id',
            'file',
            'location',
            'caption',
            'comments',
            'likes',
        )


class CommentSerializer(serializers.ModelSerializer):

    image = ImageSerializer()

    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):

    image = ImageSerializer()

    class Meta:
        model = Like
        fields = '__all__'
