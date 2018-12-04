from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):

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
        )


class ExploreUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'profile_image',
            'username',
            'name',
        )
