from django.urls import path
from . import views

app_name = 'blog'

urlpatterns=[
    path('',views.post_list,name="post_list"),
    # path('<slug:slug>/',views.PostDetail.as_view(),name="post_detail"),
    path('<slug:post>/',views.post_detail,name="post_detail"),
    path('comment/reply/', views.reply_page, name="reply"),
    path('tag/<slug:tag_slug>/',views.post_list, name='post_tag'), #this
]