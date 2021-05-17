from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import PostListSerializer, PostDetailSerialiser, CommentSerializer
from blog.models import Comment, Post
from .pagination import MyLimitOffsetPagination, MyPageNumberPagination

class PostListAPIView(ListAPIView):
    serializer_class = PostListSerializer
    pagination_class = MyPageNumberPagination
    queryset = Post.objects.all()

class PostDetailAPIView(RetrieveAPIView):
    serializer_class = PostDetailSerialiser
    lookup_field = 'slug'
    queryset = Post.objects.all()
    
class CommentListAPIView(ListAPIView):
    serializer_class = CommentSerializer
    pagination_class = MyPageNumberPagination
    queryset = Comment.objects.all()