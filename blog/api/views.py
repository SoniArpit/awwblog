from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import PostListSerializer
from blog.models import Comment, Post
from .pagination import MyLimitOffsetPagination, MyPageNumberPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Post
from rest_framework.views import APIView


class PostAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostListSerializer(posts, many=True)
        return Response({"status": 200, "payload": serializer.data})

    def post(self, request):
        # data = request.data
        # print(data)
        serializer = PostListSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({"status": 403, "errors": serializer.errors, "msg": "Something went wrong!"})

        serializer.save()

        return Response({"status": 200, "msg": "posted successfully"})

    def put(self, request):
        pass

    def patch(self, request):
        try:
            post_obj = Post.objects.get(id=request.data['id'])

            serializer = PostListSerializer(post_obj, data=request.data, partial=True)

            if not serializer.is_valid():
                return Response({"status": 403,  "errors": serializer.errors, "msg": "Something went wrong!"})

            serializer.save()
            return Response({"status": 200, "payload ":serializer.data, "msg": "patched successfully"})
        except Exception as e:
            return Response({"status": 403, 'msg': "invalid id"})


    def delete(self, request):
        pass
