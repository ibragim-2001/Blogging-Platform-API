from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import *
from .models import *


class PostsView(APIView):

    def get(self, request):
        try:
            posts = Post.objects.all()
            serializer = PostSerializer(posts, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)