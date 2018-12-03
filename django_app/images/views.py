from rest_framework.views import APIView
from rest_framework.response import Response

from db.models import Image, Comment, Like
from images.serializers import ImageSerializer, CommentSerializer, LikeSerializer


class Feed(APIView):

    def get(self, request, format=None):

        user = request.user

        following_users = user.following.all()

        print(following_users)

        return Response(status=200)
