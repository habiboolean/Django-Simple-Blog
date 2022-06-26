from django.urls import path, include
from .views import *

urlpatterns = [
    path('', PostList.as_view()),
    path('create/', PostCreate.as_view()),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),

]
