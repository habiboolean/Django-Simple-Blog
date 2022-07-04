from django.urls import path, include
from rest_framework import routers

from .views import *

app_name = 'blog'

router = routers.DefaultRouter()
router.register(r'users', UserListViewSet, basename='users')
router.register(r'posts', PostListViewSet, basename='posts')

urlpatterns = [
    path('', PostList.as_view()),
    path('api/', include(router.urls)),
    path('author/<int:author_id>/', PostListUser.as_view(), name='author_filter'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('edit/<slug:slug>/', PostEdit.as_view(), name='post_edit'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]
