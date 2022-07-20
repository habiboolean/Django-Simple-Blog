from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import Http404, HttpResponseNotFound
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views import generic
from rest_framework import viewsets, permissions, generics
from rest_framework.decorators import api_view

import Blog.models
from .models import Post
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *


class UserListViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostListViewSet(viewsets.ModelViewSet):
    class Meta:
        model = models.Post
        fields = ('title_image', 'slug')

    queryset = Post.objects.all().order_by('-created_date')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'status']
    serializer_class = PostListSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def create(self, request, *args, **kwargs):
    #     file = request.data['file']
    #     Post.objects.create(title_image=file)
    #     super().create(self,request,*args,**kwargs)


class PostList(generic.ListView):
    queryset = \
        Post.objects\
            .filter(status=Post.PostStatus.PUBLIC)\
            .order_by('-created_date')\
            .select_related()\
            .values('title', 'content', 'description', 'author_id', 'author__username', 'created_date', 'slug')
    paginate_by = 5
    template_name = 'post_list.html'


class PostListUser(generic.ListView):
    paginate_by = 5
    template_name = 'post_list_user.html'

    def get_queryset(self):
        queryset = QuerySet
        if self.kwargs['author_id'] is not self.request.user.pk:
            queryset = Post.objects \
                .filter(author=self.kwargs['author_id'], status=Post.PostStatus.PUBLIC) \
                .order_by('-created_date') \
                .select_related() \
                .values('title', 'content', 'description', 'author_id', 'author__username', 'created_date', 'slug', 'status')
        else:
            queryset = Post.objects \
                .filter(author=self.kwargs['author_id']) \
                .order_by('-created_date') \
                .select_related() \
                .values('title', 'content', 'description', 'author_id', 'author__username', 'created_date', 'slug',
                        'status')

        return queryset


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.status == Blog.models.Post.PostStatus.PRIVATE:
            if obj.author != self.request.user:
                return HttpResponseNotFound("You are not allowed to see this Post")
        return super(PostDetail, self).dispatch(request, args, kwargs)


class PostCreate(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ['title', 'title_image', 'content', 'description', 'status']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'slug': self.object.slug})


class PostEdit(LoginRequiredMixin, generic.UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'title_image', 'content', 'description', 'status']

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise Http404("You are not allowed to edit this Post")
        return super(PostEdit, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'slug': self.object.slug})
