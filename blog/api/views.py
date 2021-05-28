from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import PostListSerializer
from blog.models import Comment, Post
from .pagination import MyLimitOffsetPagination, MyPageNumberPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from ..models import Post 

@api_view(["GET"])
def home(request):
    posts = Post.objects.all()
    serailizers = PostListSerializer(posts, many=True)
    return Response({"status":200, "data":serailizers.data})

@api_view(["POST"])
def post_blogpost(request):
    data = request.data
    # print(data)
    serializer = PostListSerializer(data = request.data)

    if not serializer.is_valid():
        return Response({"status":403, "errors":serializer.errors,"msg":"Something went wrong!"})

    serializer.save()        

    return Response({"status":200, "data":data, "msg":"posted successfully"})

@api_view(["PUT"])
def update_blogpost(request, id):
    try:
        post_obj = Post.objects.get(id=id)

        serializer = PostListSerializer(post_obj, data = request.data)

        if not serializer.is_valid():
            return Response({"status":403, "errors":serializer.errors,"msg":"Something went wrong!"})

        serializer.save()        

        return Response({"status":200, "data":data, "msg":"posted successfully"})
    except Exception as e:
        return Response({"status":403, 'msg':"invalid id"})

@api_view(["DELETE"])
def delete_blogpost(request, id):
    try:
        post_obj = Post.objects.get(id=id)
        post_obj.delete()
        return Response({"status":200, "msg":"delete successfully"})
    except Exception as e:
        return Response({"status":403, 'msg':"invalid id"})

