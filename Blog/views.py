from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseNotFound
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views import generic

import Blog.models
from .models import Post


class PostList(generic.ListView):
    queryset = \
        Post.objects\
            .filter(status=Post.PostStatus.PUBLIC)\
            .order_by('-created_date')\
            .select_related()\
            .values('title', 'content', 'description', 'author__username', 'created_date', 'slug')
    template_name = 'post_list.html'


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
