from django.urls import path
app_name = "blog_api"
from . import views

urlpatterns = [
    path('', views.PostListAPIView.as_view(), name="post_list_api"),
    path('comments/',views.CommentListAPIView.as_view(), name="comments_api"),
    path('<slug:slug>/', views.PostDetailAPIView.as_view(), name="post_detail_api"),

]