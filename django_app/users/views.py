from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ExploreUserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class ExploreUsers(APIView):

    def get(self, request, format=None):

        last_five = User.objects.all().order_by('-date_joined')[:5]

        serializer = ExploreUserSerializer(last_five, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
