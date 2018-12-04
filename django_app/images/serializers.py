from django.contrib.auth import get_user_model
from rest_framework import serializers
from db.models import Image, Comment, Like

__all__ = (
    'ImageSerializer',
    'CommentSerializer',
    'LikeSerializer',
)

User = get_user_model()


class UserProfileImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = (
            'id',
            'file',
            'comment_count',
            'like_count',
        )


class FeedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username',
            'profile_image',
        )


class CommentSerializer(serializers.ModelSerializer):

    creator = FeedUserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = (
            'id',
            'message',
            'creator',
        )


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True)
    creator = FeedUserSerializer()

    class Meta:
        model = Image
        fields = (
            'id',
            'file',
            'location',
            'caption',
            'comments',
            'like_count',
            'creator',
        )
