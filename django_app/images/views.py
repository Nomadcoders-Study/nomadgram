from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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

        sorted_list = sorted(image_list, key=lambda image: image.created_at, reverse=True)

        serializer = ImageSerializer(sorted_list, many=True)

        return Response(serializer.data)


class LikeImage(APIView):

    def get(self, request, image_id, format=None):

        user = request.user

        try:
            image = Image.objects.get(id=image_id)
        except Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            preexisiting_like = Like.objects.get(
                creator=user,
                image=image,
            )
            preexisiting_like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            new_like = Like.objects.create(
                creator=user,
                image=image,
            )
            return Response(status=status.HTTP_201_CREATED)
