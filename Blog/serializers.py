from django.utils.text import slugify

from rest_framework import serializers

from Blog import models
from accounts.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'email', 'is_superuser', 'is_active', 'date_joined', 'last_login']


class PostListSerializer(serializers.ModelSerializer):

    slug = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='blog:posts-detail', read_only=True)


    class Meta:
        model = models.Post
        fields = ['url', 'id', 'title', 'slug', 'title_image', 'author', 'content', 'created_date', 'status']

    # adding and saving slug to data
    def save(self, **kwargs):
        self.validated_data['slug'] = slugify(self.validated_data['title'])
        return super(PostListSerializer, self).save()

    # Getting details url only on list view, not in details or edit view
    # Simply removing 'url' from fields if we got id argument in url
    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')
        if request is not None and request.parser_context.get('kwargs'):
            fields.pop('url', None)
        return fields

    def get_slug(self, post: models.Post):
        return slugify(post.title)

    # def get_detail_url(self, post: models.Post):
    #     request = self.context.get('request')
    #     post_id = post.id
    #     return request.build_absolute_uri(post_id)
