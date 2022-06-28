from django.urls import path, include
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', PostList.as_view()),
    path('author/<int:author_id>/', PostListUser.as_view(), name='author_filter'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('edit/<slug:slug>/', PostEdit.as_view(), name='post_edit'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]
