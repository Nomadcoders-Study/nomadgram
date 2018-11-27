from rest_framework.views import APIView
from rest_framework.response import Response

from db.models import Images
from images.serializers import ImageSerializer


class ListAllImages(APIView):

    def get(self, request, format=None):
        print(1)
        all_images = Images.objects.all()
        serializer = ImageSerializer(all_images, many=True)

        return Response(data=serializer.data)
