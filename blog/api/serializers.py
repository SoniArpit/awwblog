from blog.models import Post, Comment
from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class PostListSerializer(TaggitSerializer,serializers.ModelSerializer):
    # slug = HyperlinkedIdentityField(view_name='blog_api:post_detail_api',lookup_field='slug')
    tags = TagListSerializerField()
    comments = CommentSerializer(many=True)
    class Meta:
        model = Post
        fields =[
            "id",
            "title",
            "slug",
            "author",
            "image",
            "body",
            "publish",
            "status",
            "tags",
            "comments"
        ]
    
    def validate(self, data):
        if len(data["body"]) < 5:
            raise serializers.ValidationError({"error": "body is too short"})
        
        return data
