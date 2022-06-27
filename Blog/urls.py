from django.urls import path, include
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', PostList.as_view()),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('edit/<slug:slug>/', PostEdit.as_view()),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]
