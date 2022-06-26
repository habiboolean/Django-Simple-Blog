from django.shortcuts import render
from django.utils.text import slugify
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    queryset = \
        Post.objects\
            .filter(status=Post.PostStatus.PUBLIC)\
            .order_by('-created_date')\
            .select_related()\
            .values('title', 'content', 'author__username', 'created_date', 'slug')
    template_name = 'post_list.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreate(generic.CreateView):
    model = Post
    success_url = '/'
    template_name = 'post_create.html'
    fields = ['title', 'title_image', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)
