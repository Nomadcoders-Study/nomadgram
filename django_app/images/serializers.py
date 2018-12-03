from django.contrib.auth import get_user_model
from rest_framework import serializers
from db.models import Image, Comment, Like

__all__ = (
    'ImageSerializer',
    'CommentSerializer',
    'LikeSerializer',
)

User = get_user_model()


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'


class FeedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username',
            'profile_image',
        )


class ImageSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True)
    likes = LikeSerializer(many=True)
    creator = FeedUserSerializer()

    class Meta:
        model = Image
        fields = (
            'id',
            'file',
            'location',
            'caption',
            'comments',
            'likes',
            'creator',
        )
