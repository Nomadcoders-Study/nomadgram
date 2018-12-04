from django.contrib.auth import get_user_model
from rest_framework import serializers

from images.serializers import UserProfileImageSerializer

User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):

    images = UserProfileImageSerializer(many=True)

    class Meta:
        model = User
        fields = (
            'username',
            'name',
            'bio',
            'website',
            'post_count',
            'followers_count',
            'following_count',
            'images',
        )


class ListUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'profile_image',
            'username',
            'name',
        )
