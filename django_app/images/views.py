from rest_framework.views import APIView
from rest_framework.response import Response

from db.models import Image, Comment, Like
from images.serializers import ImageSerializer, CommentSerializer, LikeSerializer


class Feed(APIView):

    def get(self, request, format=None):

        user = request.user

        following_users = user.following.all()

        image_list = []

        for following_user in following_users:

            user_images = following_user.images.all()[:2]

            for image in user_images:

                image_list.append(image)

        sorted_list = sorted(image_list, key=get_key, reverse=True)

        serializer = ImageSerializer(sorted_list, many=True)

        return Response(serializer.data)


def get_key(image):
    return image.created_at
