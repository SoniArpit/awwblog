from blog.models import Post, Comment
from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField, PrimaryKeyRelatedField
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)

class PostListSerializer(TaggitSerializer,ModelSerializer):
    slug = HyperlinkedIdentityField(view_name='blog_api:post_detail_api',
                                   lookup_field='slug')
    tags = TagListSerializerField()
    class Meta:
        model = Post
        fields =[
            "id",
            "title",
            "slug",
            "author",
            "image",
            "publish",
            "status",
            "tags",
        ]

class PostDetailSerialiser(TaggitSerializer, ModelSerializer):
    tags = TagListSerializerField()
    # comments = SerializerMethodField()
   
    class Meta:
        model = Post
        fields =[
            "id",
            "title",
            "slug",
            "author",
            "image",
            "body",
            "tags",
            "publish",
            "status",
            # "comments"
        ]
        
    # def get_comments(self, obj):
    #     comments = Comment.objects.all()
        
    #     return CommentSerializer(comments, many=True).data


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "id",
            "post",
            "name",
            "email",
            "parent",
            "body",
            "active",
            "created"
        ]
